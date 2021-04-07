matchgreek : Simply tells you which greek letters are already used in a LaTeX file.

The idea is based on [a tweet by @IvanWerning](https://twitter.com/IvanWerning/status/1255091491275526145)
*WARNING: Very preliminary script. Use with skepticsm.*
Please let me know if something goes wrong [by opening an issue on Github](https://github.com/seyhunsaral/matchgreek/issues) or by sending me a message on twitter [@aliseyhunsaral](https://www.twitter.com/aliseyhunsaral)

### Requirements
* `python3` installation 
* `pip` (if you will install using Option I below)

### Installation & Usage
#### Option I - install with `pip`

* Install `matchgreek` package using `pip3` (or pip depending on your system) 
```
pip3 install matchgreek
```
* Run `matchgreek` from the command line  
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
* Run the script with `python3` (or `python` depending on your system)
```
python3 matchgreek.py path/to/file
```
### Sample output
```
 $ matchgreek my_latex_file.tex   # (or python matchgreek.py my_latex_file.tex 
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

### TODO
TODO Scan the files included with `\input` and `\include`
