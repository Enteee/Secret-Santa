{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
  packages = with pkgs; [
    python3Packages.ipdb
  ];
  inputsFrom = with pkgs; [
    (pkgs.callPackage ./default.nix {})
  ];
}
