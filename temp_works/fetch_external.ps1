[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$ErrorActionPreference = "Continue"

$dest = "D:\projects\Bio_Digital_Core\Temp\research\external"
$logFile = "D:\projects\Bio_Digital_Core\Temp\research\fetch_external.log"

function Log($msg) {
    $ts = Get-Date -Format "HH:mm:ss"
    Add-Content $logFile "$ts $msg" -Encoding UTF8
}

function Fetch($url, $filename) {
    $outPath = "$dest\$filename"
    if (Test-Path $outPath) { Log "SKIP exists: $filename"; return }
    try {
        Log "DL: $filename from $url"
        Invoke-WebRequest -Uri $url -OutFile $outPath -UseBasicParsing -TimeoutSec 120
        $size = (Get-Item $outPath).Length
        if ($size -lt 10000) {
            Remove-Item $outPath -Force
            Log "  FAIL: too small ($([math]::Round($size/1KB))KB) - likely HTML error page"
        } else {
            Log "  OK: $([math]::Round($size/1KB))KB"
        }
    } catch {
        if (Test-Path $outPath) { Remove-Item $outPath -Force -ErrorAction SilentlyContinue }
        Log "  ERR: $($_.Exception.Message.Substring(0, [Math]::Min(80, $_.Exception.Message.Length)))"
    }
}

Log "=== START external literature fetch ==="

# 1. Guo et al. - On Calibration of Modern Neural Networks (ICML 2017) - arXiv
Fetch "https://arxiv.org/pdf/1706.04599.pdf" "01_Guo_et_al_2017_On_Calibration_of_Modern_Neural_Networks.pdf"

# 2. Brier G.W. - Verification of Forecasts (1950) - classic paper
# Available from AMS journals
Fetch "https://journals.ametsoc.org/downloadpdf/journals/mwre/78/1/1520-0493_1950_078_0001_vofeit_2_0_co_2.pdf" "02_Brier_1950_Verification_of_Forecasts_Expressed_in_Terms_of_Probability.pdf"

# 3. Geifman & El-Yaniv - Selective Classification for Deep Neural Networks (NIPS 2017) - arXiv
Fetch "https://arxiv.org/pdf/1705.08500.pdf" "03_Geifman_ElYaniv_2017_Selective_Classification_for_Deep_Neural_Networks.pdf"

# 4. Traub et al. - Overcoming Common Flaws in Evaluation of Selective Classification - arXiv 2024
Fetch "https://arxiv.org/pdf/2403.15961.pdf" "04_Traub_et_al_2024_Overcoming_Common_Flaws_Evaluation_Selective_Classification.pdf"

# 5. Belnap N.D. - A Useful Four-Valued Logic (1977) - classic, try multiple sources
Fetch "https://link.springer.com/content/pdf/10.1007/978-94-010-1161-7_2.pdf" "05_Belnap_1977_A_Useful_Four-Valued_Logic.pdf"

# 6. Bimbo K. - Four-valued Logic - Stanford Encyclopedia / book chapter
# This is likely a book; try ResearchGate or similar
Fetch "https://iep.utm.edu/wp-content/media/Four-valued-Logic.pdf" "06_Bimbo_Four-valued_Logic.pdf"

# 7. Geisel W.A. - Tutorial on Reed-Solomon Error Correction Coding - NASA TM
Fetch "https://ntrs.nasa.gov/api/citations/19900019023/downloads/19900019023.pdf" "07_Geisel_Tutorial_Reed_Solomon_Error_Correction_Coding.pdf"

# 8. Freeman J.C. - Introduction to Forward Error Correcting Coding - NASA TM
Fetch "https://ntrs.nasa.gov/api/citations/19980228329/downloads/19980228329.pdf" "08_Freeman_Introduction_Forward_Error_Correcting_Coding.pdf"

# 9. Organick et al. - Random Access in Large-Scale DNA Data Storage (Nature Biotech 2018)
Fetch "https://www.biorxiv.org/content/biorxiv/early/2018/03/07/114553.full.pdf" "09_Organick_et_al_2018_Random_Access_Large_Scale_DNA_Data_Storage.pdf"

# 10. Lin et al. - Dynamic and Scalable DNA-based Information Storage (Nature Comm 2020)
Fetch "https://www.nature.com/articles/s41467-020-16145-2.pdf" "10_Lin_et_al_2020_Dynamic_Scalable_DNA_Information_Storage.pdf"

# 11. Heckel et al. - A Characterization of the DNA Data Storage Channel (2019) - arXiv
Fetch "https://arxiv.org/pdf/1803.03322.pdf" "11_Heckel_et_al_2019_Characterization_DNA_Data_Storage_Channel.pdf"

# 12. Squillero & Tonda - Divergence of Character and Premature Convergence (Swarm and Evolutionary 2016)
Fetch "https://arxiv.org/pdf/1511.07782.pdf" "12_Squillero_Tonda_2016_Divergence_Character_Premature_Convergence.pdf"

Log "=== DONE ==="
Get-ChildItem $dest -Filter "*.pdf" | Select-Object Name, @{N="KB";E={[math]::Round($_.Length/1KB)}} | Format-Table -AutoSize
