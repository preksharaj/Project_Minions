SHELL=/bin/bash
VERSION=$(shell cat VERSION)
PROJECT_DIR=$(abspath $(dir $(firstword $(MAKEFILE_LIST))))
TOOLCHAIN_DIR=$(TOOLCHAIN_HOME)

.PHONY: abort
ifeq ($(TOOLCHAIN_HOME),)
abort:
	@echo "Please download Tool-chain repository and run `make`"
	$(error TOOLCHAIN_HOME is not set)
endif

.PHONY: all
all: abort info

.PHONY: add_git_hooks
add_git_hooks:
	$(shell cp $(TOOLCHAIN_DIR)/git_hooks/hook/pre-commit ./.git/hooks/)
	$(shell cp -rf $(TOOLCHAIN_DIR)/git_hooks/scripts .)

.PHONY: init
init: add_git_hooks
	$(shell touch $(PROJECT_DIR)/README.md)
	$(shell touch $(PROJECT_DIR)/CHANGELOG.md)
	$(shell rm -f $(PROJECT_DIR)/CHANGELOG.md)
	$(shell touch $(PROJECT_DIR)/CHANGELOG.md)
	$(shell echo "## [Unreleased]" >> $(PROJECT_DIR)/CHANGELOG.md)
	$(shell echo "### Added" >> $(PROJECT_DIR)/CHANGELOG.md)
	$(shell echo - comments for new additions >> $(PROJECT_DIR)/CHANGELOG.md)
	$(shell echo "### Changed" >> $(PROJECT_DIR)/CHANGELOG.md)
	$(shell echo - comments for changes >> $(PROJECT_DIR)/CHANGELOG.md)

.PHONY: info
info:
	@echo "===================================================================="
	@echo "VERSION         ::: $(VERSION)"
	@echo "PROJECT ROOT    ::: $(PROJECT_DIR)"
	@echo "TOOLCHAIN HOME  ::: $(TOOLCHAIN_DIR)"
	@echo "===================================================================="
