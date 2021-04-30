
format: src/*/*.py tests/*.py
	black $^

.PHONY: format