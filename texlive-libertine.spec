%global tl_name libertine
%global tl_revision 77682
%global tl_version 5.3.0

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	Use of Linux Libertine and Biolinum fonts with LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/libertine
License:	gpl ofl lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/libertine.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/libertine.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(fontaxes)
Requires:	texlive(iftex)
Requires:	texlive(mweights)
Requires:	texlive(xkeyval)
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
The package provides the Libertine and Biolinum fonts in both Type 1 and
OTF styles, together with support macros for their use. Monospaced and
display fonts, and the "keyboard" set are also included, in OTF style,
only. The mweights package is used to manage the selection of font
weights. The package supersedes both the libertineotf and the libertine-
legacy packages.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from libertine:
Map libertine.map
TL_DROPIN_EOF
