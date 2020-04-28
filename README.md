matchgreek : Simply tells you which greek letters you used in LaTeX

The idea is based on the tweet by @IvanWerning
Very preliminary script. Use with skepticsm. Requires `python3`

### Usage 

* Elone the repostitory locally 
```
 git clone https://github.com/seyhunsaral/matchgreek.git
```
* Change the working directory to the repository dir
```
cd matchgreek
```
* Run script with `pyhton` (or `python3` depending on your system 
```
python matchgreek.py FILEPATH`
```




#### Sample output 
`python matchgreek.py my_tex_file.tex`

```
matchgreek v.0.1
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
