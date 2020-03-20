# gulpless

This is package of gulp + less, so less can be converted to css/.min.css. This is helper artifact to create accurate css for card models.

```bash
# image build
docker build -t butuzov/gulpless . --no-cache
# image usage
docker run --rm -v "$(pwd):/work/app/" butuzov/gulpless
```
