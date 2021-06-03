build-image:
	docker build -t demo-parser:latest .

# push-image:
# 	docker push

gen-test-file:
	python -m src.parser.generator ./tests/data/input_normal.dat 10 "<"

run-acceptance-test:
	python -m pytest tests/acceptance -vv
