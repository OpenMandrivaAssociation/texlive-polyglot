# revision 15878
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-polyglot
Version:	20111103
Release:	6
Summary:	TeXLive polyglot package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/polyglot.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/polyglot.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/polyglot.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive polyglot package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/polyglot/polyglot.cfg
%{_texmfdistdir}/tex/latex/polyglot/polyglot.def
%{_texmfdistdir}/tex/latex/polyglot/polyglot.sty
%doc %{_texmfdistdir}/doc/latex/polyglot/sample.dvi
%doc %{_texmfdistdir}/doc/latex/polyglot/sample.tex
#- source
%doc %{_texmfdistdir}/source/latex/polyglot/langs/english.ld
%doc %{_texmfdistdir}/source/latex/polyglot/langs/french.ld
%doc %{_texmfdistdir}/source/latex/polyglot/langs/french.ot1
%doc %{_texmfdistdir}/source/latex/polyglot/langs/german.ld
%doc %{_texmfdistdir}/source/latex/polyglot/langs/german.ot1
%doc %{_texmfdistdir}/source/latex/polyglot/langs/r_hebrew.ld
%doc %{_texmfdistdir}/source/latex/polyglot/langs/spanish.ld
%doc %{_texmfdistdir}/source/latex/polyglot/langs/spanish.ot1
%doc %{_texmfdistdir}/source/latex/polyglot/polyglot.dtx
%doc %{_texmfdistdir}/source/latex/polyglot/polyglot.ins
%doc %{_texmfdistdir}/source/latex/polyglot/polyglot.ltx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111103-2
+ Revision: 755019
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111103-1
+ Revision: 719284
- texlive-polyglot
- texlive-polyglot
- texlive-polyglot
- texlive-polyglot

