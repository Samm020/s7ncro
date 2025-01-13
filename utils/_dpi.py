import ctypes

class DPIScale:
    @staticmethod
    def set_dpi_aware():
        """set the process as dpi aware to handle scaling correctly"""
        try:
            # try to use the most modern dpi awareness api windows 10 1607+
            awareness = ctypes.c_int()
            errorCode = ctypes.windll.shcore.GetProcessDpiAwareness(0, ctypes.byref(awareness))

            # success
            if errorCode == 0:

                # if not already dpi aware
                if awareness.value == 0:
                    PROCESS_PER_MONITOR_DPI_AWARE_V2 = 2
                    ctypes.windll.shcore.SetProcessDpiAwareness(PROCESS_PER_MONITOR_DPI_AWARE_V2)
            else:
                # fallback to older method
                ctypes.windll.user32.SetProcessDPIAware()
        except Exception as e:
            print(f'failed to set dpi awareness: {e}')

    @staticmethod
    def get_scaling_factor():
        """retrieve scaling factor for primary monitor"""
        try:
            # get dpi awareness to ensure we are getting the real value
            DPIScale.set_dpi_aware()

            # use ShCore.dll for most accurate dpi detection
            MDT_EFFECTIVE_DPI = 0
            monitor = ctypes.windll.user32.MonitorFromWindow(0, 2)

            # define structures
            class POINT(ctypes.Structure):
                _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]

            # get dpi values
            dpiX = ctypes.c_uint()
            dpiY = ctypes.c_uint()

            # use GetDpiForMonitor for per monitor dpi
            ctypes.windll.shcore.GetDpiForMonitor(
                monitor,
                MDT_EFFECTIVE_DPI,
                ctypes.byref(dpiX),
                ctypes.byref(dpiY)
            )

            # return the scaling factor
            return dpiX.value / 96.0

        # fallback for older systems
        except AttributeError:

            # get device context for the screen
            hdc = ctypes.windll.user32.GetDC(0)

            # windows LOGPIXELSX has a value of 88 and is passed to the GetDeviceCaps function which retrieves device specific metrics
            # it measures the density of pixels horizontally on a screen apparently
            dpi = ctypes.windll.gdi32.GetDeviceCaps(hdc, 88)
            ctypes.windll.user32.ReleaseDC(0, hdc)

            return dpi / 96.0

        # default to 100% scaling if something goes wrong
        except Exception as e:
            print(f'failed to get scaling factor: {e}')
            return 1.0

    @staticmethod
    def adjust_for_scaling(value, scaling_factor=None):
        """adjust a value or a list of values for DPI scaling."""
        if scaling_factor is None:
            scaling_factor = DPIScale.get_scaling_factor()
        if isinstance(value, (list, tuple)):
            return [int(v * scaling_factor) for v in value]
        return int(value * scaling_factor)
