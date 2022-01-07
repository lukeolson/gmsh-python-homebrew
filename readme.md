#### Usage

```
pip install git+https://github.com/lukeolson/gmsh-python-homebrew
```

#### What

This is a simple wrapper to install [gmsh](https://gmsh.info/)'s Python interface without
building a separate binary, relying `homebrew install gmsh`.

#### Why

[Homebrew's gmsh forumla](https://github.com/Homebrew/homebrew-core/blob/HEAD/Formula/gmsh.rb)
builds `gmsh` on both `x86` and `arm64`, constructing the [gmsh Python interface](https://gitlab.onelab.info/gmsh/gmsh/-/blob/master/api/gmsh.py)
along the way.  This `setup.py` finds this file and allows installation via `pip` without rebuilding (or requiring the correct wheels; currently wheels are not available for Apple silicon).
