%{?_javapackages_macros:%_javapackages_macros}
Name:           jetty-assembly-descriptors
Version:        1.0
Release:        9.0%{?dist}
Summary:        Jetty assembly descriptors used for building


License:        ASL 2.0 or EPL
URL:            https://www.eclipse.org/jetty/
Source0:        http://git.eclipse.org/c/jetty/org.eclipse.jetty.toolchain.git/snapshot/%{name}-%{version}.tar.bz2
BuildArch:      noarch

Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
Source2:        http://www.eclipse.org/legal/epl-v10.html

BuildRequires:  jpackage-utils
BuildRequires:  maven-local
BuildRequires:  jetty-toolchain
BuildRequires:  maven-surefire-provider-junit

Requires:       maven
Requires:       jpackage-utils
Requires:       jetty-toolchain

%description
Jetty assembly descriptors used for building

%prep
%setup -q
cp -p %{SOURCE1} %{SOURCE2} .

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE-2.0.txt epl-v10.html

%changelog
* Mon Aug  5 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0-9
- Update to latest packaging guidelines

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0-6
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Oct 17 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-5
- Install license files

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov  4 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0-2
- Added missing BR on maven-surefire-provider-junit

* Thu Nov  3 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0-1
- Initial version of the package
