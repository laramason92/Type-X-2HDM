# This file was automatically created by FeynRules 2.3.32
# Mathematica version: 11.3.0 for Mac OS X x86 (64-bit) (March 7, 2018)
# Date: Sat 25 May 2019 13:29:14



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
a1 = Parameter(name = 'a1',
               nature = 'external',
               type = 'real',
               value = 0.1,
               texname = '\\alpha _1',
               lhablock = '2 HDMSBLOCK',
               lhacode = [ 1 ])

a2 = Parameter(name = 'a2',
               nature = 'external',
               type = 'real',
               value = 0.1,
               texname = '\\alpha _2',
               lhablock = '2 HDMSBLOCK',
               lhacode = [ 2 ])

a3 = Parameter(name = 'a3',
               nature = 'external',
               type = 'real',
               value = 0.1,
               texname = '\\alpha _3',
               lhablock = '2 HDMSBLOCK',
               lhacode = [ 3 ])

tanb = Parameter(name = 'tanb',
                 nature = 'external',
                 type = 'real',
                 value = 0.1,
                 texname = 't_{\\beta }',
                 lhablock = '2 HDMSBLOCK',
                 lhacode = [ 4 ])

vev3 = Parameter(name = 'vev3',
                 nature = 'external',
                 type = 'real',
                 value = 500.,
                 texname = 'v_3',
                 lhablock = '2 HDMSBLOCK',
                 lhacode = [ 5 ])

m12 = Parameter(name = 'm12',
                nature = 'external',
                type = 'real',
                value = 100.,
                texname = 'm_{12}',
                lhablock = '2 HDMSBLOCK',
                lhacode = [ 6 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymdo = Parameter(name = 'ymdo',
                 nature = 'external',
                 type = 'real',
                 value = 0.00504,
                 texname = '\\text{ymdo}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 1 ])

ymup = Parameter(name = 'ymup',
                 nature = 'external',
                 type = 'real',
                 value = 0.00255,
                 texname = '\\text{ymup}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 2 ])

yms = Parameter(name = 'yms',
                nature = 'external',
                type = 'real',
                value = 0.101,
                texname = '\\text{yms}',
                lhablock = 'YUKAWA',
                lhacode = [ 3 ])

ymc = Parameter(name = 'ymc',
                nature = 'external',
                type = 'real',
                value = 1.27,
                texname = '\\text{ymc}',
                lhablock = 'YUKAWA',
                lhacode = [ 4 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

yme = Parameter(name = 'yme',
                nature = 'external',
                type = 'real',
                value = 0.000511,
                texname = '\\text{yme}',
                lhablock = 'YUKAWA',
                lhacode = [ 11 ])

ymm = Parameter(name = 'ymm',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{ymm}',
                lhablock = 'YUKAWA',
                lhacode = [ 13 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

Me = Parameter(name = 'Me',
               nature = 'external',
               type = 'real',
               value = 0.000511,
               texname = '\\text{Me}',
               lhablock = 'MASS',
               lhacode = [ 11 ])

MMU = Parameter(name = 'MMU',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{MMU}',
                lhablock = 'MASS',
                lhacode = [ 13 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MU = Parameter(name = 'MU',
               nature = 'external',
               type = 'real',
               value = 0.00255,
               texname = 'M',
               lhablock = 'MASS',
               lhacode = [ 2 ])

MC = Parameter(name = 'MC',
               nature = 'external',
               type = 'real',
               value = 1.27,
               texname = '\\text{MC}',
               lhablock = 'MASS',
               lhacode = [ 4 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MD = Parameter(name = 'MD',
               nature = 'external',
               type = 'real',
               value = 0.00504,
               texname = '\\text{MD}',
               lhablock = 'MASS',
               lhacode = [ 1 ])

MS = Parameter(name = 'MS',
               nature = 'external',
               type = 'real',
               value = 0.101,
               texname = '\\text{MS}',
               lhablock = 'MASS',
               lhacode = [ 3 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

Mh1 = Parameter(name = 'Mh1',
                nature = 'external',
                type = 'real',
                value = 125,
                texname = '\\text{Mh1}',
                lhablock = 'MASS',
                lhacode = [ 25 ])

Mh2 = Parameter(name = 'Mh2',
                nature = 'external',
                type = 'real',
                value = 150,
                texname = '\\text{Mh2}',
                lhablock = 'MASS',
                lhacode = [ 35 ])

MhS = Parameter(name = 'MhS',
                nature = 'external',
                type = 'real',
                value = 270,
                texname = '\\text{MhS}',
                lhablock = 'MASS',
                lhacode = [ 4000005 ])

MA0 = Parameter(name = 'MA0',
                nature = 'external',
                type = 'real',
                value = 250,
                texname = '\\text{MA0}',
                lhablock = 'MASS',
                lhacode = [ 36 ])

MHP = Parameter(name = 'MHP',
                nature = 'external',
                type = 'real',
                value = 250,
                texname = '\\text{MHP}',
                lhablock = 'MASS',
                lhacode = [ 37 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

Wh1 = Parameter(name = 'Wh1',
                nature = 'external',
                type = 'real',
                value = 0.00407,
                texname = '\\text{Wh1}',
                lhablock = 'DECAY',
                lhacode = [ 25 ])

Wh2 = Parameter(name = 'Wh2',
                nature = 'external',
                type = 'real',
                value = 10.85,
                texname = '\\text{Wh2}',
                lhablock = 'DECAY',
                lhacode = [ 35 ])

WS = Parameter(name = 'WS',
               nature = 'external',
               type = 'real',
               value = 20.85,
               texname = '\\text{WS}',
               lhablock = 'DECAY',
               lhacode = [ 4000005 ])

WA0 = Parameter(name = 'WA0',
                nature = 'external',
                type = 'real',
                value = 20.85,
                texname = '\\text{WA0}',
                lhablock = 'DECAY',
                lhacode = [ 36 ])

WHP = Parameter(name = 'WHP',
                nature = 'external',
                type = 'real',
                value = 20.85,
                texname = '\\text{WHP}',
                lhablock = 'DECAY',
                lhacode = [ 37 ])

cb = Parameter(name = 'cb',
               nature = 'internal',
               type = 'real',
               value = '1/cmath.sqrt(1 + tanb**2)',
               texname = 'c_{\\beta }')

RA1x1 = Parameter(name = 'RA1x1',
                  nature = 'internal',
                  type = 'real',
                  value = 'cmath.cos(a1)*cmath.cos(a2)',
                  texname = '\\text{RA1x1}')

RA1x2 = Parameter(name = 'RA1x2',
                  nature = 'internal',
                  type = 'real',
                  value = 'cmath.cos(a2)*cmath.sin(a1)',
                  texname = '\\text{RA1x2}')

RA1x3 = Parameter(name = 'RA1x3',
                  nature = 'internal',
                  type = 'real',
                  value = 'cmath.sin(a2)',
                  texname = '\\text{RA1x3}')

RA2x1 = Parameter(name = 'RA2x1',
                  nature = 'internal',
                  type = 'real',
                  value = '-(cmath.cos(a3)*cmath.sin(a1)) - cmath.cos(a1)*cmath.sin(a2)*cmath.sin(a3)',
                  texname = '\\text{RA2x1}')

RA2x2 = Parameter(name = 'RA2x2',
                  nature = 'internal',
                  type = 'real',
                  value = 'cmath.cos(a1)*cmath.cos(a3) - cmath.sin(a1)*cmath.sin(a2)*cmath.sin(a3)',
                  texname = '\\text{RA2x2}')

RA2x3 = Parameter(name = 'RA2x3',
                  nature = 'internal',
                  type = 'real',
                  value = 'cmath.cos(a2)*cmath.sin(a3)',
                  texname = '\\text{RA2x3}')

RA3x1 = Parameter(name = 'RA3x1',
                  nature = 'internal',
                  type = 'real',
                  value = '-(cmath.cos(a1)*cmath.cos(a3)*cmath.sin(a2)) + cmath.sin(a1)*cmath.sin(a3)',
                  texname = '\\text{RA3x1}')

RA3x2 = Parameter(name = 'RA3x2',
                  nature = 'internal',
                  type = 'real',
                  value = '-(cmath.cos(a3)*cmath.sin(a1)*cmath.sin(a2)) - cmath.cos(a1)*cmath.sin(a3)',
                  texname = '\\text{RA3x2}')

RA3x3 = Parameter(name = 'RA3x3',
                  nature = 'internal',
                  type = 'real',
                  value = 'cmath.cos(a2)*cmath.cos(a3)',
                  texname = '\\text{RA3x3}')

sb = Parameter(name = 'sb',
               nature = 'internal',
               type = 'real',
               value = 'tanb/cmath.sqrt(1 + tanb**2)',
               texname = 's_{\\beta }')

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

mu2 = Parameter(name = 'mu2',
                nature = 'internal',
                type = 'real',
                value = 'm12/(cb*sb)',
                texname = '\\text{mu2}')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

lam6 = Parameter(name = 'lam6',
                 nature = 'internal',
                 type = 'real',
                 value = '(Mh1**2*RA1x3**2 + Mh2**2*RA2x3**2 + MhS**2*RA3x3**2)/vev3**2',
                 texname = '\\text{lam6}')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/ee',
                texname = 'v')

lam1 = Parameter(name = 'lam1',
                 nature = 'internal',
                 type = 'real',
                 value = '(Mh1**2*RA1x1**2 + Mh2**2*RA2x1**2 + MhS**2*RA3x1**2 - mu2*sb**2)/(cb**2*vev**2)',
                 texname = '\\text{lam1}')

lam2 = Parameter(name = 'lam2',
                 nature = 'internal',
                 type = 'real',
                 value = '(-(cb**2*mu2) + Mh1**2*RA1x2**2 + Mh2**2*RA2x2**2 + MhS**2*RA3x2**2)/(sb**2*vev**2)',
                 texname = '\\text{lam2}')

lam3 = Parameter(name = 'lam3',
                 nature = 'internal',
                 type = 'real',
                 value = '(2*MHP**2 - mu2 + (Mh1**2*RA1x1*RA1x2 + Mh2**2*RA2x1*RA2x2 + MhS**2*RA3x1*RA3x2)/(cb*sb))/vev**2',
                 texname = '\\text{lam3}')

lam4 = Parameter(name = 'lam4',
                 nature = 'internal',
                 type = 'real',
                 value = '(MA0**2 - 2*MHP**2 + mu2)/vev**2',
                 texname = '\\text{lam4}')

lam5 = Parameter(name = 'lam5',
                 nature = 'internal',
                 type = 'real',
                 value = '(-MA0**2 + mu2)/vev**2',
                 texname = '\\text{lam5}')

lam7 = Parameter(name = 'lam7',
                 nature = 'internal',
                 type = 'real',
                 value = '(Mh1**2*RA1x1*RA1x3 + Mh2**2*RA2x1*RA2x3 + MhS**2*RA3x1*RA3x3)/(cb*vev*vev3)',
                 texname = '\\text{lam7}')

lam8 = Parameter(name = 'lam8',
                 nature = 'internal',
                 type = 'real',
                 value = '(Mh1**2*RA1x2*RA1x3 + Mh2**2*RA2x2*RA2x3 + MhS**2*RA3x2*RA3x3)/(sb*vev*vev3)',
                 texname = '\\text{lam8}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/vev',
               texname = '\\text{yb}')

yc = Parameter(name = 'yc',
               nature = 'internal',
               type = 'real',
               value = '(ymc*cmath.sqrt(2))/vev',
               texname = '\\text{yc}')

ydo = Parameter(name = 'ydo',
                nature = 'internal',
                type = 'real',
                value = '(ymdo*cmath.sqrt(2))/vev',
                texname = '\\text{ydo}')

ye = Parameter(name = 'ye',
               nature = 'internal',
               type = 'real',
               value = '(yme*cmath.sqrt(2))/vev',
               texname = '\\text{ye}')

ym = Parameter(name = 'ym',
               nature = 'internal',
               type = 'real',
               value = '(ymm*cmath.sqrt(2))/vev',
               texname = '\\text{ym}')

ys = Parameter(name = 'ys',
               nature = 'internal',
               type = 'real',
               value = '(yms*cmath.sqrt(2))/vev',
               texname = '\\text{ys}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vev',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vev',
                 texname = '\\text{ytau}')

yup = Parameter(name = 'yup',
                nature = 'internal',
                type = 'real',
                value = '(ymup*cmath.sqrt(2))/vev',
                texname = '\\text{yup}')

m11 = Parameter(name = 'm11',
                nature = 'internal',
                type = 'real',
                value = '(m12*sb)/cb + (-(cb**2*lam1*vev**2) - (lam3 + lam4 + lam5)*sb**2*vev**2 - lam7*vev3**2)/2.',
                texname = '\\text{m11}')

m22 = Parameter(name = 'm22',
                nature = 'internal',
                type = 'real',
                value = '(cb*m12)/sb + (-(cb**2*(lam3 + lam4 + lam5)*vev**2) - lam2*sb**2*vev**2 - lam8*vev3**2)/2.',
                texname = '\\text{m22}')

m3 = Parameter(name = 'm3',
               nature = 'internal',
               type = 'real',
               value = '(-(cb**2*lam7*vev**2) - lam8*sb**2*vev**2 - lam6*vev3**2)/2.',
               texname = '\\text{m3}')

I1a11 = Parameter(name = 'I1a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ydo',
                  texname = '\\text{I1a11}')

I1a22 = Parameter(name = 'I1a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ys',
                  texname = '\\text{I1a22}')

I1a33 = Parameter(name = 'I1a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yb',
                  texname = '\\text{I1a33}')

I2a11 = Parameter(name = 'I2a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yup',
                  texname = '\\text{I2a11}')

I2a22 = Parameter(name = 'I2a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yc',
                  texname = '\\text{I2a22}')

I2a33 = Parameter(name = 'I2a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt',
                  texname = '\\text{I2a33}')

I3a11 = Parameter(name = 'I3a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yup',
                  texname = '\\text{I3a11}')

I3a22 = Parameter(name = 'I3a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yc',
                  texname = '\\text{I3a22}')

I3a33 = Parameter(name = 'I3a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt',
                  texname = '\\text{I3a33}')

I4a11 = Parameter(name = 'I4a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ydo',
                  texname = '\\text{I4a11}')

I4a22 = Parameter(name = 'I4a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ys',
                  texname = '\\text{I4a22}')

I4a33 = Parameter(name = 'I4a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yb',
                  texname = '\\text{I4a33}')

