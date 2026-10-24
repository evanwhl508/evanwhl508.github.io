#!/usr/bin/env python3
"""Compatibility entry point. The provisional identity has been retired."""
from pathlib import Path
import runpy
runpy.run_path(str(Path(__file__).with_name('build-brand-production.py')),run_name='__main__')
