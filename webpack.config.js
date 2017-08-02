var ExtractTextPlugin = require('extract-text-webpack-plugin')
var CopyWebpackPlugin = require('copy-webpack-plugin')
var webpack = require('webpack')
var path = require('path')
var autoprefixer = require('autoprefixer')

var config = {
  entry: {
    adhocracy4: [
      './liqd_product/assets/scss/style.scss',
      './liqd_product/assets/js/app.js'
    ],
    vendor: [
      'classnames',
      'font-awesome/scss/font-awesome.scss',
      'jquery',
      'js-cookie',
      'moment',
      'moment/locale/de.js',
      'react',
      'immutability-helper',
      'react-dom',
      'react-flip-move',
      'shariff',
      'shariff/build/shariff.min.css'
    ],
    leaflet: [
      'leaflet',
      'leaflet/dist/leaflet.css'
    ],
    datepicker: [
      './liqd_product/assets/js/init-picker.js',
      'datepicker/css/datepicker.min.css'
    ],
    'leaflet.draw': [
      'leaflet-draw',
      'leaflet-draw/dist/leaflet.draw.css'
    ]
  },
  devtool: 'eval',
  output: {
    libraryTarget: 'this',
    library: '[name]',
    path: path.resolve('./liqd_product/static/'),
    publicPath: '/static/',
    filename: '[name].js'
  },
  externals: {
    'django': 'django'
  },
  module: {
    noParse: /\.min\.js$/,
    loaders: [
      {
        test: /\.jsx?$/,
        exclude: /node_modules\/(?!adhocracy4|bootstrap)/, // exclude all dependencies but adhocracy4 and bootstrap
        loader: 'babel-loader',
        query: {
          presets: ['babel-preset-es2015', 'babel-preset-react'].map(require.resolve)
        }
      },
      {
        test: /\.s?css$/,
        loader: ExtractTextPlugin.extract('style?sourceMap', '!css?sourceMap!postcss?sourceMap!sass?sourceMap')
      },
      {
        test: /fonts\/.*\.(svg|woff2?|ttf|eot|otf)(\?.*)?$/,
        loader: 'file-loader?name=fonts/[name].[ext]'
      },
      {
        test: /\.svg$|\.png$/,
        loader: 'file-loader?name=images/[name].[ext]'
      }
    ]
  },
  postcss: [
    autoprefixer({browsers: ['last 3 versions', 'ie >= 10']})
  ],
  resolve: {
    extensions: ['', '.js', '.jsx', '.scss', '.css'],
    alias: {
      'jquery$': 'jquery/dist/jquery.min.js'
    },
    // when using `npm link`, dependencies are resolved against the linked
    // folder by default. This may result in dependencies being included twice.
    // Setting `resolve.root` forces webpack to resolve all dependencies
    // against the local directory.
    root: path.resolve('./node_modules')
  },
  resolveLoader: {
    root: path.resolve('./node_modules')
  },
  plugins: [
    new webpack.IgnorePlugin(/^\.\/locale$/, /moment$/),
    new webpack.optimize.CommonsChunkPlugin('vendor', 'vendor.js'),
    new ExtractTextPlugin('[name].css'),
    new CopyWebpackPlugin([
      {
        from: './liqd_product/assets/images/**/*',
        to: 'images/',
        flatten: true
      },
      {
        from: './liqd_product/assets/js/popover.js',
        to: 'js/',
        flatten: false
      }
    ])
  ]
}

module.exports = config
