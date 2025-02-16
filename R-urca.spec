%global packname  urca
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.2.8
Release:          2
Summary:          Unit root and cointegration tests for time series data
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/urca_1.2-8.tar.gz
Requires:         R-methods 
Requires:         R-nlme R-graphics R-stats 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-methods
BuildRequires:    R-nlme R-graphics R-stats 
BuildRequires:    blas-devel
BuildRequires:    lapack-devel

%description
Unit root and cointegration tests encountered in applied econometric
analysis are implemented.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/License
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/MacKinnonLicense.txt
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/Rcmdr
%{rlibdir}/%{packname}/book-ex
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
