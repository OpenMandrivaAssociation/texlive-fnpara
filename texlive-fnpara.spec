Name:		texlive-fnpara
Version:	25607
Release:	2
Summary:	Footnotes in paragraphs
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fnpara
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fnpara.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fnpara.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Typeset footnotes in run-on paragraphs, instead of one above
another; this is a re-seating, for the LaTeX environment, of an
example in the TeXbook. The same basic code, improved for use
in e-TeX-based LaTeX, appears in the comprehensive footnote
package footmisc, and superior versions are also available in
the manyfoot and bigfoot packages.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/fnpara
%doc %{_texmfdistdir}/doc/latex/fnpara

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
