matchgreek : Simply tells you which greek letters you used in LaTeX

The idea is based on a tweet by @IvanWerning  
WARNING: Very preliminary script. Use with skepticsm.   

### Requirements
* `python3` installation 
* `pip` (if you will install using option I)

### Installation & Usage
#### Option I - install with `pip`
I pushed the package to pip. If you install using pip. The advantage is you can run the script directly with command `matchgreek`.

* Install `matchgreek` package using `pip` (or pip3 depending on your system) 
```
pip install matchgreek
```
* Run `matchgreek` from command line  
```
matchgreek path/to/file/
```

#### Option II - Download & run the script
* Clone the repostitory on your local machine
```
 git clone https://github.com/seyhunsaral/matchgreek.git
```
* Change the working directory to the repository dir
```
cd matchgreek
```
* Run script with `pyhton` (or `python3` depending on your system)
```
python matchgreek.py path/to/file
```
#### Sample output
```
 $ matchgreek ~/my_latex_file.tex   # (or python matchgreek.py ~/my_latex_file.tex 
                                       # if you installed using Option II)

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
ps. it is open-source. feel free to modify, distribute or send a pull request
