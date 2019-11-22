using CefSharp;
using CefSharp.WinForms;
using mshtml;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace BBusted
{
    public partial class BUSTED : Form
    {
        private int gameNum = 2547470;
        private int gameNumStop = 2547468;
        private readonly ChromiumWebBrowser browser = null;
        private string result = "";

        [Obsolete]
        public BUSTED()
        {
            InitializeComponent();
            Cef.Initialize(new CefSettings());
            browser = new ChromiumWebBrowser();
            browser.FrameLoadEnd += WebBrowserFrameLoadEnded;
            panel1.Controls.Add(browser);
            browser.Dock = DockStyle.Fill;
        }

        private void LoadNext(ChromiumWebBrowser browser)
        {
            gameNum -= 1;
            if (gameNum == gameNumStop)
                StopProcess();
            else
                browser.Load("https://www.bustabit.com/game/" + gameNum.ToString());
        }

        private void StopProcess()
        {
            string path = Environment.GetFolderPath(Environment.SpecialFolder.DesktopDirectory) + "\\";
            string path2 = gameNum + "-" + Num.Text + ".csv";
            System.IO.File.WriteAllText(path + path2, result, Encoding.Default);
        }

        private void WebBrowserFrameLoadEnded(object sender, FrameLoadEndEventArgs e)
        {
            var browser = sender as ChromiumWebBrowser;
            if (e.Frame.IsMain)
                IsThere(browser);
        }

        private void IsThere(ChromiumWebBrowser browser, bool end = false)
        {
            //browser.ViewSource();
            Extension.Delay(2000);
            browser.GetSourceAsync().ContinueWith(taskHtml2 =>
            {
                var html = taskHtml2.Result;
                if (!html.Contains("<span class=\"key-muted\">"))
                {
                    if (end)
                    {
                        StopProcess();
                        MessageBox.Show("ERROR:" + gameNum.ToString());
                    }
                    else
                        IsThere(browser, true);
                }
                else
                {
                    makeData(html);
                    LoadNext(browser);
                }
            });
        }
        
        private void makeData(string shtml)
        {
            var newLine = gameNum.ToString() + ",";

            var busted_at = shtml
                .Split("<span class=\"key-muted\">Busted at: </span>")[1]
                .Split("<span class=\"bold\"> ")[1]
                .Split("</span>")[0]
                .Replace("x","");
            newLine += busted_at + ",";

            var data = shtml
               .Split("<tbody>")[1]
               .Split("</tbody>>")[0];
            

            var betResult = 0;
            var betArr = data.Split("</a></td><td>");

            foreach (var tmp in betArr)
            {
                try
                {
                    var tmpN = tmp.Split("</td>")[0].Replace(",", "");
                    betResult += Int32.Parse(tmpN);
                }
                catch
                {

                }
            }
            newLine += betResult.ToString() + ",";


            var profitResult = 0;
            var profitArr = data.Split("x</td><td>");

            foreach (var tmp in profitArr)
            {
                try
                {
                    var tmpN = tmp.Split("</td>")[0].Replace(",","");
                    if (tmpN.Contains("-"))
                    {
                        tmpN = tmpN.Replace("-", "");
                        profitResult -= Int32.Parse(tmpN);
                    }
                    else
                    {
                        profitResult += Int32.Parse(tmpN);
                    }
                }
                catch
                {

                }
            }
            profitArr = data.Split("-</td><td>");

            foreach (var tmp in profitArr)
            {
                try
                {
                    var tmpN = tmp.Split("</td>")[0].Replace(",", "");
                    if (tmpN.Contains("-"))
                    {
                        tmpN = tmpN.Replace("-", "");
                        profitResult -= Int32.Parse(tmpN);
                    }
                    else
                    {
                        profitResult += Int32.Parse(tmpN);
                    }
                }
                catch
                {

                }
            }
            newLine += profitResult.ToString();


            result += newLine + "\n";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            LoadNext(browser);
        }

        private void Num_TextChanged(object sender, EventArgs e)
        {
            var textbox = sender as TextBox;
            try
            {
                var num = Int32.Parse(textbox.Text);
                gameNum = num;
            }
            catch
            {
                textbox.Text = "";
            }
        }

        private void Num2_TextChanged(object sender, EventArgs e)
        {
            var textbox = sender as TextBox;
            try
            {
                var num = Int32.Parse(textbox.Text);
                gameNumStop = num;
            }
            catch
            {
                textbox.Text = "";
            }
        }

        
    }
}
