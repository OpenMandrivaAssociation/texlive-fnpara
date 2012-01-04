# revision 17273
# category Package
# catalog-ctan /macros/latex/contrib/fnpara
# catalog-date 2010-03-09 13:05:51 +0100
# catalog-license other-free
# catalog-version undef
Name:		texlive-fnpara
Version:	20100309
Release:	2
Summary:	Footnotes in paragraphs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fnpara
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fnpara.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fnpara.doc.tar.xz
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
%{_texmfdistdir}/tex/latex/fnpara/fnpara.sty
%doc %{_texmfdistdir}/doc/latex/fnpara/fnpara-doc.pdf
%doc %{_texmfdistdir}/doc/latex/fnpara/fnpara-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
