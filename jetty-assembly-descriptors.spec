Name:           jetty-assembly-descriptors
Version:        1.1
Release:        1
Summary:        Jetty assembly descriptors used for building


License:        ASL 2.0 or EPL
URL:            https://www.eclipse.org/jetty/
Source0:        https://github.com/jetty/jetty.toolchain/archive/refs/tags/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:	python
# Literal, so the first rpmbuild -bs records them before sysjar is installed.
BuildRequires:	maven
BuildRequires:	java-current-devel
BuildSystem:	maven

Source1:        https://www.apache.org/licenses/LICENSE-2.0.txt
Source2:        https://www.eclipse.org/legal/epl/epl-v10.html

Requires:       javapackages-filesystem

%description
Jetty assembly descriptors used for building

%prep
%setup -q -n jetty-toolchain-%{name}-%{version}
# The tag is the whole toolchain reactor. Publish this module on its own.
python - <<'PY'
import re
import shutil
from pathlib import Path
root = Path(".").resolve()
mod = root / "%{name}"
if mod.is_dir():
    stage = root.parent / ("%{name}-module")
    if stage.exists():
        shutil.rmtree(stage)
    shutil.copytree(mod, stage)
    for child in list(root.iterdir()):
        if child.is_dir():
            shutil.rmtree(child)
        else:
            child.unlink()
    for child in list(stage.iterdir()):
        shutil.move(str(child), root / child.name)
    shutil.rmtree(stage)
path = root / "pom.xml"
text = path.read_text()
text = re.sub(r"\s*<parent>.*?</parent>", "", text, count=1, flags=re.S)
head, sep, tail = text.partition("<artifactId>")
if sep and "<groupId>" not in head:
    text = head + "<groupId>org.eclipse.jetty.toolchain</groupId>\n  " + sep + tail
path.write_text(text)
PY
cp -p %{SOURCE1} %{SOURCE2} .

%files -f .mfiles
%doc LICENSE-2.0.txt epl-v10.html
