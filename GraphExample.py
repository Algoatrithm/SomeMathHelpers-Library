from Derivative import Derivatives
from  Derivative import NumericalAnalysis

# f(x) = −2x^5−3x^2+5x−1

coe = [-2, -3, 5, -1]
exp = [5, 2, 1, 0]

# Original function
fofx = [coe, exp]

# Higher order Derivatives
fofx_I = Derivatives.derive_power(fofx[0], fofx[1])
fofx_II = Derivatives.derive_power(fofx_I[0], fofx_I[1])
fofx_III = Derivatives.derive_power(fofx_II[0], fofx_II[1])
fofx_IV = Derivatives.derive_power(fofx_III[0], fofx_III[1])
fofx_V = Derivatives.derive_power(fofx_IV[0], fofx_IV[1])

print("Derivatives")
print("f^I(x) = " + str(fofx_I))
print("f^II(x) = " + str(fofx_II))
print("f^III(x) = " + str(fofx_III))
print("f^IV(x) = " + str(fofx_IV))
print("f^V(x) = " + str(fofx_V))

# Subtituting x0 = -1
x0 = -1
fofx0 = Derivatives.f_of_x(fofx[0], fofx[1], x0)

print("Evauated Functions")
print(fofx0)

NumericalAnalysis.get_taylor_series_as_graph(coe, exp, x0, fofx0)