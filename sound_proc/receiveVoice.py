import pyaudio
import wave

class voice:

  def __init__(self,SECONDS):
    self.FORMAT = pyaudio.paInt16
    self.CHANNELS = 1
    self.RATE = 16000
    self.CHUNK = 1024
    self.RECORD_SECONDS = SECONDS

  def getVoice(self):
    pa = pyaudio.PyAudio()
    stream = pa.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True, frames_per_buffer=self.CHUNK)
    print('start recording')

    data = []
    for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
      buf = stream.read(self.CHUNK)
      data.append(buf)

    print('stop recording')

    stream.stop_stream()
    stream.close()
    pa.terminate()

    out = wave.open('file.wav','wb')
    out.setnchannels(self.CHANNELS)
    out.setsampwidth(pa.get_sample_size(self.FORMAT))
    out.setframerate(self.RATE)
    out.writeframes(b''.join(data))
    out.close()

if __name__ == '__main__':
  v = voice(3)
  v.getVoice()