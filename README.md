# 中文报告/作业/幻灯片的LaTeX模板
## 配置LaTeX环境
1. 安装一个LaTeX发行版。我用的是TeX Live 2019，现在已经有最新的2020版了。可以从[国内镜像](https://mirrors.tuna.tsinghua.edu.cn/CTAN/systems/texlive/Images/)下载。
2. （可选）配置一个高颜值的开发环境，例如：
* [TeXstudio](http://texstudio.sourceforge.net/)（如果下载速度慢可复制链接到迅雷下载）
* [VS code + LaTeX Workshop](https://github.com/James-Yu/LaTeX-Workshop)（注意要把配置里的`%DOC%`改为`%DOCFILE%`，否则会出现无法识别中文路径的问题）

## report-template  
中文实验报告/课程作业模板<br>
适用于：一般性的实验报告、课程作业等<br>
不适用于：有明确格式规定的正式论文
### 使用方法：
1. 修改report-template.tex中的正文内容和reference.bib中的引文内容
2. 连续执行下面4个命令（注意需要用`xelatex`编译）<br>
`xelatex report-template.tex`<br>
`bibtex report-template.aux`<br>
`xelatex report-template.tex`<br>
`xelatex report-template.tex`<br>
如果没有引文，则注释掉report-template.tex中的bibtex配置，只需用`xelatex`编译即可
3. 代码在Window10 + TeX Live 2019下测试通过。在macOS或Linux上由于字体库的问题，第83行的`\setCJKmainfont{宋体}`可能会报错，可根据您的系统调整设置或直接注释掉，这样会使用默认的中文字体，一般在正文环境下也是宋体，但其他环境可能不一样，例如在我的电脑上，去掉这行后算法伪代码中的条件会变为楷体

## homework-template
中文作业模板<br>
适用于：网课作业等
### 使用方法：
1. 修改homework-template.tex中的作业内容
2. `xelatex homework-template.tex`（注意需要用`xelatex`编译）
3. 字体问题同上

## slide-template
中文幻灯片模板<br>
适用于：各种presentation
### 使用方法：
1. 修改slide-template.tex中的正文内容和reference.bib中的引文内容
2. 连续执行下面4个命令（注意需要用`xelatex`编译）<br>
`xelatex slide-template.tex`<br>
`bibtex slide-template.aux`<br>
`xelatex slide-template.tex`<br>
`xelatex slide-template.tex`<br>
如果没有引文，则注释掉slide-template.tex中的bibtex配置，只需用`xelatex`编译即可
3. 字体用的是`beamer`自带的那套，目前未发现问题
