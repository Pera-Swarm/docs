
install:
	uv sync

serve: clean
	uv run sphinx-autobuild . _site

build: clean
	uv run sphinx-build -b html . _site

test:
	uv run sphinx-build -W -b html . _site

clean:
	rm -rf _site

emptyCommit:
	git pull
	git commit --allow-empty -m "Empty commit (Force rebuild)"
	git push

run: clean
	uv run sphinx-build -b html . _site
