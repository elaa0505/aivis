Artificial Intelligence Virtual Interview System<br><br>

# 개발 환경
**리눅스**<br>
우분투<br><br>

**자바**<br>
OpenJDK 8<br><br>

**파이썬**<br>
KoNLPy - 한국어 정보처리<br>
scikit-learn - 머신러닝<br><br>

# 자바 설치 (서버)
**APT 업데이트**<br>
sudo apt-get update<br><br>

**자바 버전 확인**<br>
java -version<br>
javac -version<br><br>

**자바 설치**<br>
sudo apt-get install openjdk-8-jdk<br>
sudo apt-get install openjdk-8-jre (jre만 원하는 경우)<br><br>

**여러 종류의 자바가 설치되어 있을시 Default Java 설정**<br>
sudo update-alternatives --config java<br><br>

**자바 환경변수 설정**<br>
1. 환경변수 설정 파일 열기<br>
sudo nano /etc/environment<br>
2. 환경변수 설정 파일에 아래 path 추가<br>
JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64"<br><br>

**환경변수 적용하기**<br>
source /etc/environment<br><br>

**환경변수 확인하기**<br>
echo $JAVA_HOME<br><br>

# 파이썬 설치 (서버)
**APT 업데이트**<br>
sudo apt-get update<br><br>

**Pyton 설치**<br>
sudo apt-get install python3<br><br>

**Pyton 버전 확인**<br>
python --version<br><br>

# 필요한 파이썬 패키지 설치 (서버)
**KoNLPy 설치**<br>
pip install jpype1<br>
pip install konlpy<br><br>

**scikit-learn**<br>
pip install scikit-learn<br><br>

# Windows 용 자바 및 파이썬 환경변수 설정
**JAVA_HOME**<br>
F:\Java\jdk1.8.0<br><br>

**CLASSPATH**<br>
%JAVA_HOME%\lib;.<br><br>

**Path**<br>
%JAVA_HOME%\bin<br>
F:\Python<br>
F:\Python\Scripts<br><br>

# Windows 에서 KoNLPy 사용시 필요한 패키지
**Microsoft Build Tools 2015 업데이트 3 (재배포 가능 패키지 및 빌드 도구)**<br>
https://visualstudio.microsoft.com/ko/vs/older-downloads/<br><br>
