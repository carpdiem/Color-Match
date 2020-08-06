import numpy as np

class Color_Match:
    def __init__(self):
        self.hc_kB = 0.0143877735
        data = np.loadtxt('lin2012xyz10_fine_7sf.csv', delimiter=',')
        self.wavelengths = data[:,0] * 10**-9
        self.s1 = data[:,1]
        self.s2 = data[:,2]
        self.s3 = data[:,3]

    def planck(self, l, t):
        """Returns the relative intensity of a Planck's Law distribution at a given wavelength (l -- in meters) and temperature (t -- in Kelvin)."""
        return 1. / l**5.0 * 1. / (np.exp(self.hc_kB / (l * t)) - 1.)

    def planck_spectrum(self, t):
        """Returns the relative intensities of the full Planck spectrum for a light source at a given temperature (t -- in Kelvin), across the entire range of human-visible frequencies, as defined in Color_Match.wavelengths ."""
        return np.array([planck(l, t) for l in self.wavelengths])

    def sense_vector(spectrum):
        """Returns the expected sensory-perception vector corresponding to the normalized (and relative) amounts of signal received on the L(ong), M(edium), and S(hort) wavelength color receptors according to the 10-deg XYZ CMFs transformed from the CIE (2006) 2-deg LMS cone fundamentals with a 0.1nm spacing from: http://cvri.ioo.ucl.ac.uk/cmfs.htm

        Return value format is as a numpy Matrix, 3x1 (aka - 3-row column vector), to facilitate use of this output with other package functions.

        Note that length(spectrum) must equal length(Color_Match.wavelengths) for this to work properly. Automatic tests and error-catching coming soon!"""
        s = np.matrix([np.sum(self.s1 * spectrum), np.sum(self.s2 * spectrum), np.sum(self.s3 * spectrum)]).T
        return s / np.max(s)

    def s_lookup(self, num, l):
        """num = 1, 2, 3 (corresponds to L(ong), M(edium), S(hort) wavelength receptors)
        l (wavelength) should be in units of meters, and lie between np.min(Color_Match.wavelengths) and np.max(Color_Match.wavelengths)"""
        if num == 1:
            s = self.s1
        elif num == 2:
            s = self.s2
        elif num == 3:
            s = s3
        return s[np.argmin((self.wavelengths - l)**2.0)]

    def rgb_composition(l1, l2, l3, sv):
        """Finds relative intensities required for light sources at l1, l2, and l3 in wavelength (meters) space to match the sense vector (sv) provided in the arguments.

        sv should be a 3x1 np.Matrix (aka - 3-row column vector). For convenience, this is the same as the output of the Color_Match.sense_vector function.

        l1, l2, l3 should have units of meters, and are most commonly the primary emission wavelengths of your RGB channels in an LED light source."""
        s_mat = np.matrix([[self.s_lookup(1, l1), self.s_lookup(1, l2), self.s_lookup(1, l3)],
                           [self.s_lookup(2, l1), self.s_lookup(2, l2), self.s_lookup(2, l3)],
                           [self.s_lookup(3, l1), self.s_lookup(3, l2), self.s_lookup(3, l3)]])
        c_mat = s_mat.I * sv
        return c_mat / np.max(c_mat)
