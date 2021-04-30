
black_marker: src/*/*.py tests/*.py
	black $?
	@touch $@
