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
        private int gameNumStop = 2547458;
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
