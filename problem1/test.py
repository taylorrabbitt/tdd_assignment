import unittest
from decomp import DecomposedUrl
from decomp import decomposeURL

class TestDecomp(unittest.TestCase):

    # make sure that there is a class for a decomposed url
    def test_decomp_object_exists(self):
        self.testDecomp = DecomposedUrl.__init__

    # check return value of decomposeURL when just entering a protocol
    def test_decomp_function_only_protocol(self):
        testReturnStr = "https" + ", " + "" + ", " + ""
        result = decomposeURL("https:")
        self.assertEqual(testReturnStr, result, "decomposeURL(\"https\") returns: https, '', '' ")
    
    # check return value of decomposeURL when just entering a domain
    def test_decomp_function_only_domain(self):
        testReturnStr = "" + ", " + "www.google.com" + ", " + ""
        result = decomposeURL("//www.google.com/")
        self.assertEqual(testReturnStr, result, "decomposeURL(\"www.google.com\") returns: '', 'www.google.com', '' ")

    # check return value of decomposeURL when just entering a path
    def test_decomp_function_only_path(self):
        testReturnStr = "" + ", " + "" + ", " + "some-path"
        result = decomposeURL("/some-path")
        self.assertEqual(testReturnStr, result, "decomposeURL(\"\some-path\") returns: '', '', 'some-path' ")

    # check return value of decomposeURL when just entering a protocol and domain
    def test_decomp_function_protocol_domain(self):
        testReturnStr = "https" + ", " + "www.google.com" + ", " + ""
        result = decomposeURL("https://www.google.com")
        self.assertEqual(testReturnStr, result, "decomposeURL(\"https://www.google.com\") returns: https, 'www.google.com', '' ")

    # check return value of decomposeURL when just entering a protocol and a path
    def test_decomp_function_protocol_path(self):
        testReturnStr = "https" + ", " + "" + ", " + "some-path"
        result = decomposeURL("https:/some-path")
        self.assertEqual(testReturnStr, result, "decomposeURL(\"https:/some-path\") returns: https, '', 'some-path' ")
    
    # check return value of decomposeURL when just entering a domain and a path
    def test_decomp_function_domain_path(self):
        testReturnStr = "" + ", " + "www.google.com" + ", " + "some-path"
        result = decomposeURL("//www.google.com/some-path")
        self.assertEqual(testReturnStr, result, "decomposeURL(\"//www.google.com/some-path\") returns: '', 'www.google.com', 'some-path' ")

    # check return value of decomposeURL when enter a protocol, domain, and a path
    def test_decomp_function_protocol_domain_path(self):
        testReturnStr = "https" + ", " + "www.google.com" + ", " + "some-path"
        result = decomposeURL("https://www.google.com/some-path")
        self.assertEqual(testReturnStr, result, "decomposeURL(\"https://www.google.com/some-path\") returns: https, 'www.google.com', 'some-path' ")


if __name__ == '__main__':
    unittest.main()