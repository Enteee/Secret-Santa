FROM nixos/nix

RUN nix-channel --add https://nixos.org/channels/nixos-25.05 nixpkgs
RUN nix-channel --update

COPY *.nix *.py /secret-santa/

RUN set -exuo pipefail \
  && nix-env -i $(nix-build secret-santa)
