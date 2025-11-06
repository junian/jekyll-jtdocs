# coding: utf-8

Gem::Specification.new do |spec|
  spec.name          = "jekyll-jtdocs"
  spec.version       = "0.10.1"
  spec.authors       = ["Patrick Marsceill", "Matthew Wang", "Junian Triajianto"]
  spec.email         = ["patrick.marsceill@gmail.com", "matt@matthewwang.me", "jt@junian.dev"]

  spec.summary       = %q{A modern, highly customizable, and responsive Jekyll theme for documentation with built-in search.}
  spec.homepage      = "https://github.com/junian/jekyll-jtdocs"
  spec.license       = "MIT"
  spec.metadata      = {
    "bug_tracker_uri"   => "https://github.com/junian/jekyll-jtdocs/issues",
    "changelog_uri"     => "https://github.com/junian/jekyll-jtdocs/blob/main/CHANGELOG.md",
    "documentation_uri" => "https://www.junian.dev/jekyll-jtdocs/",
    "source_code_uri"   => "https://github.com/junian/jekyll-jtdocs",
  }

  spec.files         = `git ls-files -z ':!:*.jpg' ':!:*.png'`.split("\x0").select { |f| f.match(%r{^(assets|bin|_layouts|_includes|lib|Rakefile|_sass|LICENSE|README|CHANGELOG|favicon)}i) }
  spec.executables   << 'jekyll-jtdocs'

  spec.add_development_dependency "bundler", ">= 2.3.5"
  spec.add_runtime_dependency "jekyll", ">= 3.8.5"
  spec.add_runtime_dependency "jekyll-seo-tag", ">= 2.0"
  spec.add_runtime_dependency "jekyll-include-cache"
  spec.add_runtime_dependency "rake", ">= 12.3.1"
end
