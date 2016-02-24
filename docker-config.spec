%if 0%{?rhel} >= 7
%global _path /etc/sysconfig/docker-network
%endif
%if 0%{?rhel} <= 6
%global _path /etc/sysconfig/docker
%endif
%global _keyword DOCKER_NETWORK_OPTIONS
%global _network 192.168.0.0
%global _cidr 24

Name:		docker-blp-config
Version:	1.0
Release:	1%{?dist}
Summary:	Change Docker's default IP space

Group:		System/Base
License:	Apache
URL:		https://github.com/zaina/docker-config

Requires:	docker

%description
This RPM changes the default IP space that Docker uses in RHEL.

#%prep
#%setup -q


#%build
#%configure


%post
# Save a backup copy of the existing docker-network config file
cp %{_path}{,.rpmsave-blp-config}
# If the docker --bip or -b parameter is specified, do not change it. Otherwise, add it as declared in the global variables.
sed -i 's/'\''/"/g; /--bip=\|-b=/! s/%{_keyword}=\("[^ "]*\)/%{_keyword}=\1 --bip=%{_range}\/%{_cidr}/; s/%{_keyword}=$/%{_keyword}="--bip=%{_network}\/%{_cidr}"/' %{_path}

%files
%doc



%changelog
