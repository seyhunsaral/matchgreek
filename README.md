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
```
 $ python3 matchgreek.py ~/my_latex_file.tex
 
matchgreek v.0.1
=====Used Letters=====
ϕ   \phi
σ   \sigma
μ   \mu
π   \pi
τ   \tau



=====Unused Letters=====
ϝ   \digamma
α   \alpha
Λ   \Lambda
Ω   \Omega
χ   \chi
ε   \varepsilon
ς   \varsigma
γ   \gamma
ω   \omega
ν   \nu
θ   \theta
Π   \Pi
ϰ   \varkappa
s   \Upsilon
ϵ   \epsilon
β   \beta
ϑ   \vartheta
Θ   \Theta
Γ   \Gamma
Δ   \Delta
Ξ   \Xi
ι   \iota
κ   \kappa
λ   \lambda
υ   \upsilon
ζ   \zeta
φ   \varphi
ϱ   \varrho
ρ   \rho
Ψ   \Psi
ξ   \xi
ϖ   \varpi
δ   \delta
ψ   \psi
Φ   \Phi
Σ   \Sigma
η   \eta
```
