import os
import sys
import requests
import subprocess
import tempfile
import shutil

class AutoUpdate:
    def __init__(self, repo_owner, repo_name, current_version):
        self.repo_owner = repo_owner
        self.repo_name = repo_name
        self.current_version = current_version
        self.api_url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest'

        if getattr(sys, 'frozen', False):
            self.current_path = os.path.abspath(sys.executable)
        else:
            self.current_path = os.path.abspath(sys.argv[0])

    def _version(self, version):
        """parse version"""
        return tuple(map(int, version.split('.')))

    def _get_exe(self, release_data):
        """get info of the exe file in assets"""
        try:
            for asset in release_data['assets']:
                if asset['name'].endswith('.exe'):
                    return asset
        except Exception:
            return None

    def _update_bat(self, temp_path, new_name):
        """creates batch script to handle theupdate process"""
        old_dir = os.path.dirname(self.current_path)
        file_path = os.path.join(old_dir, new_name)

        batch_script = f'''
        @echo off

        REM close the old version of the application if running
        echo closing old version
        taskkill /im "{os.path.basename(self.current_path)}" /t /f > nul 2>&1
        timeout /t 1 /nobreak > nul

        REM retry deleting the old version until successful
        :retry_delete
        echo deleting old version
        del "{self.current_path}" 2>nul
        if exist "{self.current_path}" (
            timeout /t 1 /nobreak > nul
            goto retry_delete
        )

        REM copy new version to the location of the old version
        echo copying new version
        copy "{temp_path}" "{file_path}"

        REM start the new version
        echo starting new version
        start "" "{file_path}"

        REM wait 1 second to ensure the new version starts before cleanup
        echo cleaning up
        timeout /t 1 /nobreak > nul

        REM remove the directory containing the downloaded temporary new version files
        rd /s /q "{os.path.dirname(temp_path)}"

        REM delete this batch file and exit, also avoids that batch file not found error :3
        (goto) 2>nul & del "%~f0"
        exit
        '''.strip()

        # write batch script to a temporary file
        batch_path = os.path.join(tempfile.gettempdir(), 's7ncro-auto-update.bat')
        with open(batch_path, 'w') as f:
            f.write(batch_script)

        return batch_path

    def check_update(self):
        """check if newer version available"""
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()

            latest_release = response.json()
            latest_version = latest_release['tag_name']

            # compare versions
            if self._version(latest_version) > self._version(self.current_version):
                exe_info = self._get_exe(latest_release)
                return {
                    'update_available': True,
                    'version': latest_version,
                    'download_url': exe_info['browser_download_url'],
                    'file_name': exe_info['name'],
                }
            return {'update_available': False}

        except Exception as e:
            return {'error': f'failed to check for updates: {str(e)}'}

    def run_update(self, download_url, file_name):
        """download the new version and prepare for install"""
        try:
            # create a temporary directory for the download
            temp_dir = tempfile.mkdtemp()
            temp_path = os.path.join(temp_dir, file_name)

            # fownload the new file
            response = requests.get(download_url, stream=True)
            response.raise_for_status()

            with open(temp_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)

            if not os.path.exists(temp_path):
                raise FileNotFoundError(f'failed to download new file to {temp_path}')

            # create update batch script
            batch_path = self._update_bat(temp_path, file_name)

            if not os.path.exists(batch_path):
                raise FileNotFoundError(f'failed to create batch script at {batch_path}')

            # run the batch script
            subprocess.Popen(f'start "" "{batch_path}"', shell=True)
            return {'success': True}

        except Exception as e:
            if 'temp_dir' in locals():
                try:
                    shutil.rmtree(temp_dir)
                except Exception:
                    pass
            return {'success': False, 'error': str(e)}
