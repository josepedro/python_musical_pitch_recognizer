import sys
import alsaaudio
import wave
import numpy
import struct

def main(argv):
	recorder = alsaaudio.PCM(alsaaudio.PCM_CAPTURE)
	recorder.setchannels(1)
	recorder.setrate(44100)
	recorder.setformat(alsaaudio.PCM_FORMAT_FLOAT_LE)
	recorder.setperiodsize(441)

	times = numpy.linspace(0, 1, 44100)
	do4 = numpy.sin(2*numpy.pi*261.63*times)
	do_s4 = numpy.sin(2*numpy.pi*277.18*times)
	re4 = numpy.sin(2*numpy.pi*293.66*times)
	re_s4 = numpy.sin(2*numpy.pi*311.13*times)
	mi4 = numpy.sin(2*numpy.pi*329.63*times)
	fa4 = numpy.sin(2*numpy.pi*349.23*times)
	fa_s4 = numpy.sin(2*numpy.pi*369.99*times)
	sol4 = numpy.sin(2*numpy.pi*392.00*times)
	sol_s4 = numpy.sin(2*numpy.pi*415.30*times)
	la4 = numpy.sin(2*numpy.pi*440.*times)
	la_s4 = numpy.sin(2*numpy.pi*466.16*times)
	si4 = numpy.sin(2*numpy.pi*493.88*times)
	notes = [do4, do_s4, re4, re_s4, mi4, fa4, fa_s4, sol4, sol_s4, la4, la_s4, si4]

	energy_notes = [0,0,0,0,0,0,0,0,0,0,0,0]
	signal_sound = []

	while True:
		for sample in range(0,10):
			l, data = recorder.read()
			buffer = list(struct.unpack('f'*441,data))
			signal_sound = signal_sound + buffer

		for note in range(0, 12):
			energy_notes[note] = numpy.sum(numpy.power(numpy.convolve(signal_sound, notes[note]), 2))

		print "max is: "
		print energy_notes.index(numpy.max(energy_notes))
		signal_sound = []
		print "begginnig other"


if __name__ == "__main__":
    main(sys.argv)
