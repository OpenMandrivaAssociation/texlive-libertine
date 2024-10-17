Name:		texlive-libertine
Version:	71061
Release:	1
Summary:	Use of Linux Libertine and Biolinum fonts with LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/libertine
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/libertine.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/libertine.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the Libertine and Biolinum fonts in both
Type 1 and OTF styles, together with support macros for their
use. Monospaced and display fonts, and the "keyboard" set are
also included, in OTF style, only. The mweights package is used
to manage the selection of font weights. The package supersedes
both the libertineotf and the libertine-legacy packages.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/enc/dvips/libertine
%{_texmfdistdir}/fonts/map/dvips/libertine
%{_texmfdistdir}/fonts/opentype/public/libertine
%{_texmfdistdir}/fonts/tfm/public/libertine
%{_texmfdistdir}/fonts/type1/public/libertine
%{_texmfdistdir}/fonts/vf/public/libertine
%{_texmfdistdir}/tex/latex/libertine
%doc %{_texmfdistdir}/doc/fonts/libertine

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
