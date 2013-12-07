# revision 25607
# category Package
# catalog-ctan /macros/latex/contrib/fnpara
# catalog-date 2012-03-11 01:08:16 +0100
# catalog-license lppl1.3
# catalog-version undef
Name:		texlive-fnpara
Version:	20120311
Release:	3
Summary:	Footnotes in paragraphs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fnpara
License:	LPPL1.3
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


%changelog
* Tue Mar 27 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120311-1
+ Revision: 787613
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20100309-2
+ Revision: 752003
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20100309-1
+ Revision: 718473
- texlive-fnpara
- texlive-fnpara
- texlive-fnpara
- texlive-fnpara

