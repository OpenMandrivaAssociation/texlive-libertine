# revision 24921
# category Package
# catalog-ctan /fonts/libertine
# catalog-date 2011-12-13 08:25:06 +0100
# catalog-license gpl
# catalog-version 5.1.3x6
Name:		texlive-libertine
Version:	5.1.3x6
Release:	4
Summary:	Use the font Libertine with LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/libertine
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/libertine.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/libertine.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The Linux-Libertine project offers a font family with a wide
range of shapes, and support of several alphabets (including
Latin, Cyrillic, Greek and Hebrew).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/opentype/public/libertine/LinBiolinum_K.otf
%{_texmfdistdir}/fonts/opentype/public/libertine/LinBiolinum_R.otf
%{_texmfdistdir}/fonts/opentype/public/libertine/LinBiolinum_RB.otf
%{_texmfdistdir}/fonts/opentype/public/libertine/LinBiolinum_RI.otf
%{_texmfdistdir}/fonts/opentype/public/libertine/LinBiolinum_aBL.otf
%{_texmfdistdir}/fonts/opentype/public/libertine/LinBiolinum_aRL.otf
%{_texmfdistdir}/fonts/opentype/public/libertine/LinBiolinum_aU.otf
%{_texmfdistdir}/fonts/opentype/public/libertine/LinBiolinum_aUB.otf
%{_texmfdistdir}/fonts/opentype/public/libertine/LinBiolinum_aUI.otf
%{_texmfdistdir}/fonts/opentype/public/libertine/LinBiolinum_aUL.otf
%{_texmfdistdir}/fonts/opentype/public/libertine/LinBiolinum_aULB.otf
%{_texmfdistdir}/fonts/opentype/public/libertine/LinBiolinum_aW.otf
%{_texmfdistdir}/fonts/opentype/public/libertine/LinBiolinum_aWB.otf
%{_texmfdistdir}/fonts/opentype/public/libertine/LinBiolinum_aWI.otf
%{_texmfdistdir}/fonts/opentype/public/libertine/LinBiolinum_aWL.otf
%{_texmfdistdir}/fonts/opentype/public/libertine/LinBiolinum_aWLB.otf
%{_texmfdistdir}/fonts/opentype/public/libertine/LinLibertine_DR.otf
%{_texmfdistdir}/fonts/opentype/public/libertine/LinLibertine_I.otf
%{_texmfdistdir}/fonts/opentype/public/libertine/LinLibertine_R.otf
%{_texmfdistdir}/fonts/opentype/public/libertine/LinLibertine_RB.otf
%{_texmfdistdir}/fonts/opentype/public/libertine/LinLibertine_RBI.otf
%{_texmfdistdir}/fonts/opentype/public/libertine/LinLibertine_RI.otf
%{_texmfdistdir}/fonts/opentype/public/libertine/LinLibertine_RZ.otf
%{_texmfdistdir}/fonts/opentype/public/libertine/LinLibertine_RZI.otf
%{_texmfdistdir}/fonts/opentype/public/libertine/LinLibertine_aBL.otf
%{_texmfdistdir}/fonts/opentype/public/libertine/LinLibertine_aDRL.otf
%{_texmfdistdir}/fonts/opentype/public/libertine/LinLibertine_aRL.otf
%{_texmfdistdir}/fonts/opentype/public/libertine/LinLibertine_aZL.otf
%{_texmfdistdir}/fonts/opentype/public/libertine/LinMono_M.otf
%{_texmfdistdir}/fonts/opentype/public/libertine/LinMono_aML.otf
%{_texmfdistdir}/tex/latex/libertine/fxbuni.inc
%{_texmfdistdir}/tex/latex/libertine/fxiuni.inc
%{_texmfdistdir}/tex/latex/libertine/fxkuni.inc
%{_texmfdistdir}/tex/latex/libertine/fxluni.inc
%{_texmfdistdir}/tex/latex/libertine/libertineotf.sty
%doc %{_texmfdistdir}/doc/fonts/libertine/Bugs.txt
%doc %{_texmfdistdir}/doc/fonts/libertine/ChangeLog.txt
%doc %{_texmfdistdir}/doc/fonts/libertine/GPL.txt
%doc %{_texmfdistdir}/doc/fonts/libertine/INSTALL.txt
%doc %{_texmfdistdir}/doc/fonts/libertine/LICENCE.txt
%doc %{_texmfdistdir}/doc/fonts/libertine/OFL.txt
%doc %{_texmfdistdir}/doc/fonts/libertine/README.libertine
%doc %{_texmfdistdir}/doc/fonts/libertine/libertine.pdf
%doc %{_texmfdistdir}/doc/fonts/libertine/libertine.sty
%doc %{_texmfdistdir}/doc/fonts/libertine/libertine.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 5.1.3x6-3
+ Revision: 753304
- Rebuild to reduce used resources

* Mon Dec 26 2011 Paulo Andrade <pcpa@mandriva.com.br> 5.1.3x6-2
+ Revision: 745273
- texlive-libertine

* Sat Dec 17 2011 Paulo Andrade <pcpa@mandriva.com.br> 5.1.3x6-1
+ Revision: 743294
- texlive-libertine

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 5.1.2-1
+ Revision: 718855
- texlive-libertine
- texlive-libertine
- texlive-libertine
- texlive-libertine

