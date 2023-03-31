Name:		texlive-musicography
Version:	53596
Release:	2
Summary:	Accessing symbols for music writing with pdfLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/musicography
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/musicography.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/musicography.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package makes available the most commonly used symbols in
writing about music in a way that can be used with pdfLaTeX and
looks consistent and attractive. It includes accidentals,
meters, and notes of different rhythmic values. The package
builds on the approach used in the harmony package, where the
symbols are taken from the MusiXTeX fonts. But it provides a
larger range of symbols and a more flexible, user-friendly
interface written using xparse and stackengine.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/musicography
%doc %{_texmfdistdir}/doc/latex/musicography

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
