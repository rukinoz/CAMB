import numpy as np
import camb

for model in ['ppf', 'fluid']:
    print(f"\n=== {model} ===")
    for xi in [-0.05, 0.0, 0.05]:
        try:
            pars = camb.set_params(
                H0=67.5, ombh2=0.022, omch2=0.122, mnu=0.06, omk=0, tau=0.06,
                As=2.1e-9, ns=0.965, xi=xi,
                dark_energy_model=model, lmax=500,
            )
            r = camb.get_results(pars)
            z = np.array([1.0, 3.0])
            Hz = r.hubble_parameter(z)
            print(f"  xi={xi:+.2f}: H(z=1)={Hz[0]:.4f}, H(z=3)={Hz[1]:.4f}")
        except Exception as e:
            print(f"  xi={xi:+.2f}: HATA {e}")
