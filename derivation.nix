{ lib
, callPackage
, python3Packages
}:
  with python3Packages;
  buildPythonApplication {

    pname = "secret-santa";
    version = "1.0";

    propagatedBuildInputs = [ flask ];

    src = ./.;
  }

