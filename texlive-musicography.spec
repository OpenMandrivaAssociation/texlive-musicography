%global tl_name musicography
%global tl_revision 77682

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Accessing symbols for music writing with pdfLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/musicography
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/musicography.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/musicography.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package makes available the most commonly used symbols in writing
about music in a way that can be used with pdfLaTeX and looks consistent
and attractive. It includes accidentals, meters, and notes of different
rhythmic values. The package builds on the approach used in the harmony
package, where the symbols are taken from the MusiXTeX fonts. But it
provides a larger range of symbols and a more flexible, user-friendly
interface written using xparse and stackengine.

