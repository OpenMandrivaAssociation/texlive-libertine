# revision 28048
# category Package
# catalog-ctan /macros/latex/contrib/libertine
# catalog-date 2012-10-22 15:44:58 +0200
# catalog-license lppl
# catalog-version 0.03
Name:		texlive-libertine
Version:	0.03
Release:	1
Summary:	Simple use of Linux Libertine and Biolinum fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/libertine
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/libertine.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/libertine.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package offers compatibility to old documents which use
\usepackage{libertine}. The package passes all options to the
packages biolinum-type1 and libertine-type1, and sets the
default font encoding to T1.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/libertine/libertine.sty
%doc %{_texmfdistdir}/doc/latex/libertine/Changes
%doc %{_texmfdistdir}/doc/latex/libertine/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
