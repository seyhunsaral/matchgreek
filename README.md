matchgreek : Simply tells you which greek letters you used in LaTeX

The idea is based on the tweet by @IvanWerning
Very preliminary script. Use with skepticsm. Requires `python3`

### Usage 

* clone the repostitory locally and enter the folder (for default `cd matchgreek`)
* run `python matchgreek.py FILEPATH`(or python3 depending on your system)

python3 matchgreek.py ../exampletex.tex                     seyhun@s-mpi-dell
matchgreek v.0.1

#### Sample output 
`python matchgreek.py my_tex_file.tex`

```
=====Used Letters=====
σ   \sigma
Ψ   \Psi
Ω   \Omega
τ   \tau
δ   \delta
ϕ   \phi
π   \pi
α   \alpha
θ   \theta



=====Unused Letters=====
η   \eta
Σ   \Sigma
ς   \varsigma
ω   \omega
s   \Upsilon
λ   \lambda
Φ   \Phi
ϵ   \epsilon
ξ   \xi
Δ   \Delta
ρ   \rho
μ   \mu
κ   \kappa
γ   \gamma
ψ   \psi
Λ   \Lambda
Θ   \Theta
Γ   \Gamma
ϰ   \varkappa
ι   \iota
Π   \Pi
ν   \nu
ϝ   \digamma
ϖ   \varpi
Ξ   \Xi
υ   \upsilon
ζ   \zeta
χ   \chi
ϱ   \varrho
ε   \varepsilon
β   \beta
φ   \varphi
ϑ   \vartheta
```
