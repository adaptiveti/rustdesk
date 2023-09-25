Name:       suporteadaptive
Version:    1.2.2
Release:    0
Summary:    RPM package
License:    GPL-3.0
Requires:   gtk3 libxcb libxdo libXfixes alsa-lib libappindicator libvdpau1 libva2 pam gstreamer1-plugins-base

%description
The best open-source remote desktop client software, written in Rust.

%prep
# we have no source, so nothing here

%build
# we have no source, so nothing here

%global __python %{__python3}

%install
mkdir -p %{buildroot}/usr/bin/
mkdir -p %{buildroot}/usr/lib/suporteadaptive/
mkdir -p %{buildroot}/usr/share/suporteadaptive/files/
mkdir -p %{buildroot}/usr/share/icons/hicolor/256x256/apps/
mkdir -p %{buildroot}/usr/share/icons/hicolor/scalable/apps/
install -m 755 $HBB/target/release/rustdesk %{buildroot}/usr/bin/suporteadaptive
install $HBB/libsciter-gtk.so %{buildroot}/usr/lib/suporteadaptive/libsciter-gtk.so
install $HBB/res/rustdesk.service %{buildroot}/usr/share/suporteadaptive/files/
install $HBB/res/128x128@2x.png %{buildroot}/usr/share/icons/hicolor/256x256/apps/suporteadaptive.png
install $HBB/res/scalable.svg %{buildroot}/usr/share/icons/hicolor/scalable/apps/suporteadaptive.svg
install $HBB/res/rustdesk.desktop %{buildroot}/usr/share/suporteadaptive/files/
install $HBB/res/rustdesk-link.desktop %{buildroot}/usr/share/suporteadaptive/files/

%files
/usr/bin/suporteadaptive
/usr/lib/suporteadaptive/libsciter-gtk.so
/usr/share/suporteadaptive/files/suporteadaptive.service
/usr/share/icons/hicolor/256x256/apps/suporteadaptive.png
/usr/share/icons/hicolor/scalable/apps/suporteadaptive.svg
/usr/share/suporteadaptive/files/suporteadaptive.desktop
/usr/share/suporteadaptive/files/suporteadaptive-link.desktop
/usr/share/suporteadaptive/files/__pycache__/*

%changelog
# let's skip this for now

# https://www.cnblogs.com/xingmuxin/p/8990255.html
%pre
# can do something for centos7
case "$1" in
  1)
    # for install
  ;;
  2)
    # for upgrade
    systemctl stop suporteadaptive || true
  ;;
esac

%post
cp /usr/share/suporteadaptive/files/suporteadaptive.service /etc/systemd/system/suporteadaptive.service
cp /usr/share/suporteadaptive/files/suporteadaptive.desktop /usr/share/applications/
cp /usr/share/suporteadaptive/files/suporteadaptive-link.desktop /usr/share/applications/
systemctl daemon-reload
systemctl enable suporteadaptive
systemctl start suporteadaptive
update-desktop-database

%preun
case "$1" in
  0)
    # for uninstall
    systemctl stop suporteadaptive || true
    systemctl disable suporteadaptive || true
    rm /etc/systemd/system/suporteadaptive.service || true
  ;;
  1)
    # for upgrade
  ;;
esac

%postun
case "$1" in
  0)
    # for uninstall
    rm /usr/share/applications/suporteadaptive.desktop || true
    rm /usr/share/applications/suporteadaptive-link.desktop || true
    update-desktop-database
  ;;
  1)
    # for upgrade
  ;;
esac
