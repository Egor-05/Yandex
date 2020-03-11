import wave
import struct


def pitch_and_toss():
    source = wave.open("in.wav", mode="rb")
    dest = wave.open("out.wav", mode="wb")

    dest.setparams(source.getparams())

    frames_count = source.getnframes()

    data = struct.unpack("<" + str(frames_count) + "h",
                         source.readframes(frames_count))

    newdata = [i for i in data if int(i) > 5 or int(i) < -5]
    a = len(data) // 4
    data1 = newdata[:a + 1]
    data2 = newdata[a + 1:a + a + 1]
    data3 = newdata[a + a + 1:a + a + a + 1]
    data4 = newdata[a + a + a + 1:]
    newdata = data3 + data4 + data1 + data2
    newframes = struct.pack("<" + str(len(newdata)) + "h", *newdata)

    dest.writeframes(newframes)
    source.close()
    dest.close()