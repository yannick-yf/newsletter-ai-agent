import unittest
import sys
import importlib

class TestPackageImports(unittest.TestCase):
    
    def test_standard_library_imports(self):
        """Test that standard library packages can be imported"""
        try:
            import openai
            import agno
        except ImportError as e:
            self.fail(f"Failed to import standard library: {e}")
    
    def test_specific_package_import(self):
        """Test importing a specific package"""
        package_name = "agno"  # Replace with your package name
        
        try:
            imported_module = importlib.import_module(package_name)
            self.assertIsNotNone(imported_module)
        except ImportError:
            self.fail(f"Failed to import {package_name}")
    
    def test_package_has_expected_attributes(self):
        """Test that imported package has expected attributes/functions"""
        import agno
        
        # Check that json module has expected functions
        self.assertTrue(hasattr(agno, 'agent'))
    
    def test_package_in_sys_modules(self):
        """Test that package appears in sys.modules after import"""
        import math
        self.assertIn('math', sys.modules)
    
    def test_import_from_package(self):
        """Test importing specific items from a package"""
        try:
            from agno.agent import Agent
            from agno.models.openai import OpenAIChat
        except ImportError as e:
            self.fail(f"Failed to import from package: {e}")

if __name__ == '__main__':
    unittest.main()