#if UNITY_EDITOR
using System;
using System.IO;
using UnityEditor;
using UnityEditor.Build.Reporting;
using UnityEditor.SceneManagement;
using UnityEngine;

namespace U003Ed
{
    // Cai dat import cho atlas U003: khong nen, khong mipmap, RGBA32 de giu nguyen alpha/mau goc.
    public class U003Importer : AssetPostprocessor
    {
        void OnPreprocessTexture()
        {
            if (!assetPath.Replace('\\', '/').Contains("Assets/Resources/U003/")) return;
            var ti = (TextureImporter)assetImporter;
            ti.textureType = TextureImporterType.Default;
            ti.alphaSource = TextureImporterAlphaSource.FromInput;
            ti.alphaIsTransparency = false;      // giu mau goc (straight alpha), khong "dilate" them
            ti.mipmapEnabled = false; ti.isReadable = false; ti.npotScale = TextureImporterNPOTScale.None;
            ti.filterMode = FilterMode.Bilinear; ti.wrapMode = TextureWrapMode.Clamp; ti.maxTextureSize = 4096;
            ti.textureCompression = TextureImporterCompression.Uncompressed;
            var def = ti.GetDefaultPlatformTextureSettings(); def.format = TextureImporterFormat.RGBA32; ti.SetPlatformTextureSettings(def);
            var and = ti.GetPlatformTextureSettings("Android"); and.overridden = true; and.format = TextureImporterFormat.RGBA32; and.maxTextureSize = 4096; ti.SetPlatformTextureSettings(and);
            var win = ti.GetPlatformTextureSettings("Standalone"); win.overridden = true; win.format = TextureImporterFormat.RGBA32; win.maxTextureSize = 4096; ti.SetPlatformTextureSettings(win);
        }
    }

    public static class U003Build
    {
        const string ScenePath = "Assets/Scenes/U003_Main.unity";

        static void MakeScene()
        {
            Directory.CreateDirectory("Assets/Scenes");
            var sc = EditorSceneManager.NewScene(NewSceneSetup.EmptyScene, NewSceneMode.Single);
            var go = new GameObject("U003"); go.AddComponent<U003.Game>();
            EditorSceneManager.SaveScene(sc, ScenePath);
            EditorBuildSettings.scenes = new[] { new EditorBuildSettingsScene(ScenePath, true) };
        }

        static void CommonSettings()
        {
            PlayerSettings.companyName = "U003"; PlayerSettings.productName = "JX1 U003";
            PlayerSettings.defaultScreenWidth = 960; PlayerSettings.defaultScreenHeight = 540;
            PlayerSettings.fullScreenMode = FullScreenMode.Windowed; PlayerSettings.resizableWindow = true;
            PlayerSettings.defaultInterfaceOrientation = UIOrientation.LandscapeLeft;
        }

        public static void BuildWindows()
        {
            MakeScene(); CommonSettings();
            Directory.CreateDirectory("D:/JX1_U003_build/win");
            var opt = new BuildPlayerOptions { scenes = new[] { ScenePath }, locationPathName = "D:/JX1_U003_build/win/JX1_U003.exe", target = BuildTarget.StandaloneWindows64, options = BuildOptions.Development };
            Finish(BuildPipeline.BuildPlayer(opt));
        }

        public static void BuildAndroid()
        {
            MakeScene(); CommonSettings();
            PlayerSettings.SetApplicationIdentifier(UnityEditor.Build.NamedBuildTarget.Android, "com.u003.jx1proto");
            PlayerSettings.Android.minSdkVersion = AndroidSdkVersions.AndroidApiLevel24;
            PlayerSettings.SetScriptingBackend(UnityEditor.Build.NamedBuildTarget.Android, UnityEditor.ScriptingImplementation.IL2CPP);
            PlayerSettings.Android.targetArchitectures = AndroidArchitecture.ARM64;
            PlayerSettings.Android.useCustomKeystore = false;      // keystore debug mac dinh cua Unity (APK thu nghiem)
            EditorUserBuildSettings.buildAppBundle = false;
            EditorUserBuildSettings.androidBuildType = AndroidBuildType.Development;
            EditorUserBuildSettings.development = true;
            EditorUserBuildSettings.SwitchActiveBuildTarget(BuildTargetGroup.Android, BuildTarget.Android);
            Directory.CreateDirectory("D:/JX1_U003_build/android");
            var opt = new BuildPlayerOptions { scenes = new[] { ScenePath }, locationPathName = "D:/JX1_U003_build/android/JX1_U003_debug.apk", target = BuildTarget.Android, options = BuildOptions.Development };
            Finish(BuildPipeline.BuildPlayer(opt));
        }

        static void Finish(BuildReport r)
        {
            Debug.Log("[U003] build " + r.summary.result + " size=" + r.summary.totalSize + " errors=" + r.summary.totalErrors + " time=" + r.summary.totalTime);
            EditorApplication.Exit(r.summary.result == BuildResult.Succeeded ? 0 : 1);
        }
    }
}
#endif
