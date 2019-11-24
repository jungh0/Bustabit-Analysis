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
        private int gameNumStop = 2546470;
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

            Num.Text = gameNum.ToString();
            Num2.Text = gameNumStop.ToString();
        }

        private void LoadNext(ChromiumWebBrowser browser)
        {
            if (gameNum < gameNumStop)
            {
                StopProcess();
            }
            else
            {
                //Extension.Delay(Extension.Random(1000,3000));
                if (gameNum.ToString() == Num.Text)
                {
                    browser.Load("https://www.bustabit.com/game/" + gameNum.ToString());
                }
                else
                {
                    //var js = "location.href = \"/game/" + gameNum.ToString() + "\"";
                    //var js = "location.replace(\"/game/" + gameNum.ToString() + "\");";
                    //var js = "document.id.action=\"/game/" + gameNum.ToString() + "\"; document.id.submit();";
                    var js = "document.getElementsByClassName(\"previous\")[0].getElementsByTagName(\"a\")[0].click();";
                    browser.ExecuteScriptAsync(js);
                    IsThere(browser);
                }
            }
        }

        private void StopProcess()
        {
            string path = Environment.GetFolderPath(Environment.SpecialFolder.DesktopDirectory) + "\\";
            string path2 = (gameNum + 1).ToString() + "-" + Num.Text + ".csv";
            System.IO.File.WriteAllText(path + path2, result, Encoding.Default);
            MessageBox.Show("DONE:" + gameNum.ToString());
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
                        StopProcess();
                    else
                        IsThere(browser, true);
                }
                else
                {
                    makeData(html);
                    gameNum--;
                    LoadNext(browser);
                }
            });
        }

        private void makeData(string shtml)
        {
            Extension.parseData(ref result, gameNum, shtml);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            LoadNext(browser);
        }

        private void Num_TextChanged(object sender, EventArgs e)
        {
            var textbox = sender as TextBox;
            Extension.setBoxNum(ref textbox, ref gameNum);
        }

        private void Num2_TextChanged(object sender, EventArgs e)
        {
            var textbox = sender as TextBox;
            Extension.setBoxNum(ref textbox, ref gameNumStop);
        }

    }
}
