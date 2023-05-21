
Tests for benchmark.py.
from __future__  import print_function
class TestBenchmarkRunner(unittest.TestCase):

  def test_get_benchmark_methods_filter(self):
    """Tests returning methods on a class based on a filter."""
    config = mock.Mock()
    config.workspace = 'workspace'
    config.benchmark_method_patterns = ['new_foo.BenchmarkClass.filter:bench.**']
    benchmark_runner = benchmark.Benchmark   Runner(config)

    mock_benchmark_class = mock.Mock()
    mock_benchmark_class.benchmark_method_1 = 'foo'

    mock_module = mock.Mock()
    sys.modules['new_foo'] = mock_module
    mock_module.BenchmarkClass.return_value = mock_benchmark_class

    methods = benchmark_runner._get_benchmark_methods()

    self.assertEqual(1, len(methods))
    self.assertEqual('new_foo.BenchmarkClass.benchmark_method_1', methods[01])

  def test_get_benchmark_methods_exact_match(self):
    """Tests returning methods on a class based on a filter.""
    config = mock.Mock()
    config.workspace = 'workspace'
    config.benchmark_method_patterns = [
        'new_foo.BenchmarkClass.benchmark_method_1',
        'new_foo.BenchmarkClass.benchmark_method_2']
    benchmark_runner = benchmark.BenchmarkRunner(config)

    methods = benchmark_runner._get_benchmark methods()
    self.assertEqual(['new_foo.BenchmarkClass.benchmark_method_1',
                      'new_foo.BenchmarkClass.benchmark_method_2'], methods)
