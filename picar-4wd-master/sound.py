import pyaudio
import time
from math import log10
import audioop  

class Sound:
    def __init__(self):
        index = 0
        self.p = pyaudio.PyAudio()
        WIDTH = 2
        RATE = int(self.p.get_device_info_by_index(index)['defaultSampleRate'])
        # DEVICE = p.get_default_input_device_info()['index']
        DEVICE = index
        self.rms = 1
        # print(self.p.get_default_input_device_info())

        def callback(in_data, frame_count, time_info, status):
            self.rms = audioop.rms(in_data, WIDTH) / 32767
            return in_data, pyaudio.paContinue


        self.stream = self.p.open(format=self.p.get_format_from_width(WIDTH),
                        input_device_index=DEVICE,
                        channels=1,
                        rate=RATE,
                        input=True,
                        output=False,
                        stream_callback=callback)

        self.stream.start_stream()

    def get_sample(self):
        if self.stream.is_active(): 
            db = 20 * log10(self.rms)
            print(f"RMS: {self.rms} DB: {db}") 
            # refresh every 0.3 seconds 
            time.sleep(0.3)
            return db
        else:
            return None

    def close_stream(self):
        self.stream.stop_stream()
        self.stream.close()

        self.p.terminate()