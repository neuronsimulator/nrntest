/* Created by Language version: 7.1.0 cacheloop */
/* VECTORIZED */
#include <stdio.h>
#include <math.h>
#include "scoplib.h"
#undef PI
#define nil 0
 
#include "md1redef.h"
#include "section.h"
#include "md2redef.h"

#if METHOD3
extern int _method3;
#endif

#include "nrncuda.h"

//#undef exp
//#define exp hoc_Exp
//extern double hoc_Exp(double d);
 
#if !defined(CACHELOOP)
#define CACHELOOP GPU_PODSIZE 
#endif
#if CACHELOOP
#define _cldec int _clj;
#define _cldecjj int _cljj=0, _clss=1;
#define _cldec0 int _clj = 0;
#define _cloff * _cls + _clj
#define _cljarg _clj,
#define _cljproto int _clj,
#define _cls CACHELOOP
#define _clb for (_clj = 0; _clj < _cls; ++_clj) {
#define _cle }
#else
 
#undef CACHELOOP
#define CACHELOOP 0
#define _cldec /**/
#define _cldecjj /**/
#define _cldec0 /**/
#define _cloff /**/
#define _cljarg /**/
#define _cljproto /**/
#define _clj 0
#define _cls 1
#define _cljj 0
#define _clss 1
#define _clb /**/
#define _cle /**/
#endif
 
typedef void(*Pvmi)(_NrnThread* _nt, _Memb_list* _ml, int);


#define _threadargscomma_ _p, _ppvar, _cljarg _thread, _nt,
#define _threadargscommakern_ _dp, _p, _ppvar, _clj,
#define _threadargs_ _p, _ppvar, _cljarg _thread, _nt
#define _threadargskern_ _dp, _p, _ppvar, _clj
 
#define _threadargsprotocomma_ double* _p, Datum* _ppvar, _cljproto Datum* _thread, _NrnThread* _nt,
#define _threadargsprotocommakern_ nrncuda_defines_t _dp, double* _p, Datum* _ppvar, int _clj, 
#define _threadargsproto_ double* _p, Datum* _ppvar, _cljproto Datum* _thread, _NrnThread* _nt
#define _threadargsprotokern_ nrncuda_defines_t _dp, double* _p, Datum* _ppvar, int _clj
 	/*SUPPRESS 761*/
	/*SUPPRESS 762*/
	/*SUPPRESS 763*/
	/*SUPPRESS 765*/
	 extern double *getarg();
 /* Thread safe. No static _p or _ppvar. */
 
#define t _nt->_t
#define dt _nt->_dt
#define gnabar _p[0 _cloff]
#define gkbar _p[1 _cloff]
#define gl _p[2 _cloff]
#define el _p[3 _cloff]
#define gna _p[4 _cloff]
#define gk _p[5 _cloff]
#define il _p[6 _cloff]
#define m _p[7 _cloff]
#define h _p[8 _cloff]
#define n _p[9 _cloff]
#define Dm _p[10 _cloff]
#define Dh _p[11 _cloff]
#define Dn _p[12 _cloff]
#define ena _p[13 _cloff]
#define ek _p[14 _cloff]
#define ina _p[15 _cloff]
#define ik _p[16 _cloff]
#define v _p[17 _cloff]
#define _g _p[18 _cloff]
#define mtau _p[19 _cloff] 
#define minf _p[20 _cloff] 
#define htau _p[21 _cloff] 
#define hinf _p[22 _cloff] 
#define ntau _p[23 _cloff] 
#define ninf _p[24 _cloff] 
#define _ion_ena	_dp._params[_ppvar[0 _cloff]._i]
#define _ion_ina	_dp._params[_ppvar[1 _cloff]._i]
#define _ion_dinadv	_dp._params[_ppvar[2 _cloff]._i]
#define _ion_ek		_dp._params[_ppvar[3 _cloff]._i]
#define _ion_ik		_dp._params[_ppvar[4 _cloff]._i]
#define _ion_dikdv	_dp._params[_ppvar[5 _cloff]._i]
 
#if MAC
#if !defined(v)
#define v _mlhv
#endif
#if !defined(h)
#define h _mlhh
#endif
#endif

extern "C" {
 static int hoc_nrnpointerindex =  -1;
 static Datum* _extcall_thread;
 static Prop* _extcall_prop;
 /* external NEURON variables */
 extern double celsius;
 /* declaration of user functions */
 static int _hoc_rates();
 static int _hoc_vtrap();
 extern int ret(double);
 static int _mechtype;

extern int nrn_get_mechtype(const char*);
extern void _nrn_cacheloop_reg(int type, int cls);
extern void hoc_register_prop_size(int type, int _psize, int _dsize);
extern void hoc_register_cuda_capable(int _type, int _capable);
extern void hoc_register_var(DoubScal* scdoub, DoubVec* vdoub, IntFunc* function);
extern void ivoc_help(char* p);
extern void hoc_register_limits(int type, HocParmLimits* limits);
extern void hoc_register_units( int type, HocParmUnits* units);
extern nrncuda_memb_prop_t nrncuda_memb_prop[30];
extern void nrn_promote(Prop* p, int conc, int rev);

static int _hoc_setdata() {
 Prop *_prop, *hoc_getdata_range(int);
 _prop = hoc_getdata_range(_mechtype);
 _extcall_prop = _prop;
 ret(1.);
 return 1;
}
 /* connect user functions to hoc names */
 static IntFunc hoc_intfunc[] = {
 "setdata_hhx", _hoc_setdata,
 "rates_hhx", _hoc_rates,
 "vtrap_hhx", _hoc_vtrap,
 0, 0
};
#define vtrap vtrap_hhx
static double vtrap ( _threadargsprotocomma_ double _lx , double _ly );

static void _check_rates(_threadargsproto_); 
static void _check_table_thread(double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt, int _type) {
  _cldec0
  // _check_rates(_threadargs_);
 }
 /* declare global and static user variables */
 static int _thread1data_inuse = 0;
static double _thread1data[6*_cls];

#define _gth 0
#define usetable usetable_hhx

 double usetable = 1;
 /* some parameters have upper and lower limits */
 static HocParmLimits _hoc_parm_limits[] = {
 "gl_hhx", 0, 1e+09,
 "gkbar_hhx", 0, 1e+09,
 "gnabar_hhx", 0, 1e+09,
 "usetable_hhx", 0, 1,
 0,0,0
};
 static HocParmUnits _hoc_parm_units[] = {
 "mtau_hhx", "ms",
 "htau_hhx", "ms",
 "ntau_hhx", "ms",
 "gnabar_hhx", "S/cm2",
 "gkbar_hhx", "S/cm2",
 "gl_hhx", "S/cm2",
 "el_hhx", "mV",
 "gna_hhx", "S/cm2",
 "gk_hhx", "S/cm2",
 "il_hhx", "mA/cm2",
 0,0
};
 static double delta_t = 0.01;
 static double h0 = 0;
 static double m0 = 0;
 static double n0 = 0;

static double minf_hhx=0;
static double mtau_hhx=0;
static double hinf_hhx=0;
static double htau_hhx=0;
static double ninf_hhx=0;
static double ntau_hhx=0;

 /* connect global user variables to hoc */
 static DoubScal hoc_scdoub[] = {
 "minf_hhx", &minf_hhx,
 "hinf_hhx", &hinf_hhx,
 "ninf_hhx", &ninf_hhx,
 "mtau_hhx", &mtau_hhx,
 "htau_hhx", &htau_hhx,
 "ntau_hhx", &ntau_hhx,
 "usetable_hhx", &usetable_hhx,
 0,0
};
 static DoubVec hoc_vdoub[] = {
 0,0,0
};
static double _sav_indep;

#define _cvode_ieq _ppvar[6]._i
 /* connect range variables in _p that hoc is supposed to know about */
 static char *_mechanism[] = {
 "7.2.0 nrncuda",
"hhx",
 "gnabar_hhx",
 "gkbar_hhx",
 "gl_hhx",
 "el_hhx",
 0,
 "gna_hhx",
 "gk_hhx",
 "il_hhx",
 0,
 "m_hhx",
 "h_hhx",
 "n_hhx",
 0,
 0};

static void nrn_alloc(Prop* _prop);
static void nrn_cur(_NrnThread* _nt, _Memb_list* _ml, int _type) ;
static void nrn_jacob(_NrnThread* _nt, _Memb_list* _ml, int _type) ;
static void nrn_state(_NrnThread* _nt, _Memb_list* _ml, int _type) ;
static void nrn_init(_NrnThread* _nt, _Memb_list* _ml, int _type) ;

static Pfri _ode_count(int _type);
static Pfri _ode_map(int _ieq, double **_pv, double **_pvdot, double *_pp, Datum* _ppd, double *_atol, int _type); 
static Pfri _ode_matsol(_NrnThread* _nt, _Memb_list* _ml, int _type);
static Pfri _ode_spec(_NrnThread* _nt, _Memb_list* _ml, int _type);

__device__ double atomicAdd(double* address, double val)
{
    double old = *address, assumed;
    do {
        assumed = old;
        old =
           __longlong_as_double(
                  atomicCAS((unsigned long long int*)address,
                            __double_as_longlong(assumed),
                            __double_as_longlong(assumed + val)));
    } while (assumed != old);
    return old;
}

static Symbol* _na_sym;
static Symbol* _k_sym;
 
Prop* need_memb_cl(Symbol* sym, int* cls, int* clj);

static void nrn_alloc(Prop *_prop)
{
	Prop *prop_ion, *need_memb();
	double *_p; Datum *_ppvar;
 	_cldec0 _cldecjj
 
	_p = nrn_prop_data_alloc_cl(_mechtype, 25, _prop, &_clj, &_ppvar, 7);

 	/*initialize range parameters*/
 	gnabar = 0.12;
 	gkbar = 0.036;
 	gl = 0.0003;
 	el = -54.3;
 	_prop->param = _p;
 	_prop->param_size = 25;

        nrncuda_memb_prop[_mechtype].param_size = 25;

 	_prop->dparam = _ppvar;
 	/*connect ionic variables to this model*/
 
	prop_ion = need_memb_cl(_na_sym, &_clss, &_cljj);
 
 nrn_promote(prop_ion, 0, 1);
 	_ppvar[0*_cls + _clj]._pval = &prop_ion->param[0*_clss + _cljj]; /* ena */
 	_ppvar[1*_cls + _clj]._pval = &prop_ion->param[3*_clss + _cljj]; /* ina */
 	_ppvar[2*_cls + _clj]._pval = &prop_ion->param[4*_clss + _cljj]; /* _ion_dinadv */
 
	prop_ion = need_memb_cl(_k_sym, &_clss, &_cljj);

 nrn_promote(prop_ion, 0, 1);
 	_ppvar[3*_cls + _clj]._pval = &prop_ion->param[0*_clss + _cljj]; /* ek */
 	_ppvar[4*_cls + _clj]._pval = &prop_ion->param[3*_clss + _cljj]; /* ik */
 	_ppvar[5*_cls + _clj]._pval = &prop_ion->param[4*_clss + _cljj]; /* _ion_dikdv */
 
	// printf("Finishing hhx alloc\n");
}

 static void _initlists();
  /* some states have an absolute tolerance */
 static Symbol** _atollist;
 static HocStateTolerance _hoc_state_tol[] = {
 0,0
};
 static void _thread_mem_init(Datum*);
 static void _thread_cleanup(Datum*);
 static void _update_ion_pointer(Datum*);
 extern void ion_reg(char *name, double valence);
 extern Symbol* hoc_lookup(char* s);
 extern void register_mech(char**, void(*)(Prop*), Pvmi, Pvmi, Pvmi, Pvmi, int, int);
 extern void _nrn_thread_reg(int i, int cons, void(*f)(Datum*));
 extern void _nrn_thread_table_reg(int i, void(*f)(double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt, int _type));
 extern void hoc_register_cvode(int i, Pfri cnt, Pfri map, Pfri spec, Pfri matsol);
 extern void hoc_register_tolerance(int type, HocStateTolerance* tol, Symbol*** stol);
 extern void _cvode_abstol( Symbol** s, double* tol, int i);

void  _hhx_reg() {
	int _vectorized = 1;
        _initlists();
 	ion_reg("na", -10000.);
 	ion_reg("k", -10000.);
 	_na_sym = hoc_lookup("na_ion");
 	_k_sym = hoc_lookup("k_ion");
 	register_mech(_mechanism, nrn_alloc,nrn_cur, nrn_jacob, nrn_state, nrn_init, hoc_nrnpointerindex, 2);
  _extcall_thread = (Datum*)ecalloc(1, sizeof(Datum));
  _thread_mem_init(_extcall_thread);
  _thread1data_inuse = 0;
 _mechtype = nrn_get_mechtype(_mechanism[1]);
 _nrn_cacheloop_reg(_mechtype, _cls);
     _nrn_thread_reg(_mechtype, 1, _thread_mem_init);
     _nrn_thread_reg(_mechtype, 0, _thread_cleanup);
     _nrn_thread_reg(_mechtype, 2, _update_ion_pointer);
     _nrn_thread_table_reg(_mechtype, _check_table_thread);
  hoc_register_prop_size(_mechtype, 25, 7);
  hoc_register_cuda_capable(_mechtype, 1);
 	hoc_register_cvode(_mechtype,(Pfri) _ode_count,(Pfri) _ode_map,(Pfri) _ode_spec,(Pfri) _ode_matsol);
 	hoc_register_tolerance(_mechtype, _hoc_state_tol, &_atollist);
 	hoc_register_var(hoc_scdoub, hoc_vdoub, hoc_intfunc);
 	ivoc_help("help ?1 hhx ./hhx.mod\n");
 hoc_register_limits(_mechtype, _hoc_parm_limits);
 hoc_register_units(_mechtype, _hoc_parm_units);
 }

 static double *_t_minf;
 static double *_t_mtau;
 static double *_t_hinf;
 static double *_t_htau;
 static double *_t_ninf;
 static double *_t_ntau;
static int _reset;
static char *modelname = "hhx.mod   squid sodium, potassium, and leak channels";

static int error;
static int _ninits = 0;
static int _match_recurse=1;
static void _modl_cleanup(){ _match_recurse=1;}
static int  _f_rates ( _threadargsprotocomma_ double _lv );
static void rates(_threadargsprotocomma_ double _lv); 
 
 static void _n_rates(_threadargsprotocomma_ double _lv);
 static int _slist1[3], _dlist1[3];
 
/*CVODE*/
 static int _ode_spec1 (_threadargsproto_) {int _reset = 0; {
   _clb rates ( _threadargscomma_ v ) ;
   _cle _clb Dm = ( minf - m ) / mtau ;
   _cle _clb Dh = ( hinf - h ) / htau ;
   _cle _clb Dn = ( ninf - n ) / ntau ;
   _cle }
 return _reset;
}
 static int _ode_matsol1 (_threadargsproto_) {
 _clb rates ( _threadargscomma_ v ) ;
 _cle _clb Dm = Dm  / (1. - dt*( ( ( ( - 1.0 ) ) ) / mtau )) ;
 _cle _clb Dh = Dh  / (1. - dt*( ( ( ( - 1.0 ) ) ) / htau )) ;
 _cle _clb Dn = Dn  / (1. - dt*( ( ( ( - 1.0 ) ) ) / ntau )) ; _cle
return 0;
}
 /*END CVODE*/

__device__ void rates_k(_threadargsprotocommakern_ double _lv);
__device__ void states_k (_threadargsprotokern_, double dt_k) { 
   rates_k ( _threadargscommakern_ v ) ;
   m = m + (1. - exp(dt_k*(( ( ( - 1.0 ) ) ) / mtau)))*(- ( ( ( minf ) ) / mtau ) / ( ( ( ( - 1.0) ) ) / mtau ) - m) ;
   h = h + (1. - exp(dt_k*(( ( ( - 1.0 ) ) ) / htau)))*(- ( ( ( hinf ) ) / htau ) / ( ( ( ( - 1.0) ) ) / htau ) - h) ;
   n = n + (1. - exp(dt_k*(( ( ( - 1.0 ) ) ) / ntau)))*(- ( ( ( ninf ) ) / ntau ) / ( ( ( ( - 1.0) ) ) / ntau ) - n) ;
}


static int states (_threadargsproto_) { {
   _clb rates ( _threadargscomma_ v ) ;
   _cle _clb  m = m + (1. - exp(dt*(( ( ( - 1.0 ) ) ) / mtau)))*(- ( ( ( minf ) ) / mtau ) / ( ( ( ( - 1.0) ) ) / mtau ) - m) ;
   _cle _clb  h = h + (1. - exp(dt*(( ( ( - 1.0 ) ) ) / htau)))*(- ( ( ( hinf ) ) / htau ) / ( ( ( ( - 1.0) ) ) / htau ) - h) ;
   _cle _clb  n = n + (1. - exp(dt*(( ( ( - 1.0 ) ) ) / ntau)))*(- ( ( ( ninf ) ) / ntau ) / ( ( ( ( - 1.0) ) ) / ntau ) - n) ;
   _cle }
  return 0;
}

static double _mfac_rates, _tmin_rates;


static void _check_rates(_threadargsproto_) {
  static int _maktable=1; int _i, _j, _ix = 0;
  double _xi, _tmax;
  static double _sav_celsius;
  if (!usetable) {return;}
  if (_sav_celsius != celsius) { _maktable = 1;}
  if (_maktable) { 
   double _x, _dx;
    _maktable=0;
   _tmin_rates =  - 100.0 ;
   _tmax =  100.0 ;
   _dx = (_tmax - _tmin_rates)/200.;
    _mfac_rates = 1./_dx;
   for (_i=0, _x=_tmin_rates; _i < 201; _x += _dx, _i++) {
    _f_rates(_threadargscomma_ _x);
    _t_minf[_i] = minf;
    _t_mtau[_i] = mtau;
    _t_hinf[_i] = hinf;
    _t_htau[_i] = htau;
    _t_ninf[_i] = ninf;
    _t_ntau[_i] = ntau;
   }
   _sav_celsius = celsius;
  }
 }

static void rates(_threadargsprotocomma_ double _lv) { 
#if 0
_check_rates(_threadargs_);
#endif
 _n_rates(_threadargscomma_ _lv);
 return;
 }

__device__ void _f_rates_k(_threadargsprotocommakern_ double _lv);
__device__ void rates_k(_threadargsprotocommakern_ double _lv) { 
//#if 0
//_check_rates(_threadargs_);
//#endif
// _n_rates(_threadargscomma_ _lv);
_f_rates_k(_threadargscommakern_ _lv);
}

 static void _n_rates(_threadargsprotocomma_ double _lv){
 int _i, _j;
 double _xi, _theta;
 if (!usetable) {
    _f_rates(_threadargscomma_ _lv); return; 
 }
 _xi = _mfac_rates * (_lv - _tmin_rates);
 _i = (int) _xi;
 if (_xi <= 0.) {
 minf = _t_minf[0];
 mtau = _t_mtau[0];
 hinf = _t_hinf[0];
 htau = _t_htau[0];
 ninf = _t_ninf[0];
 ntau = _t_ntau[0];
 return; }
 if (_xi >= 200.) {
 minf = _t_minf[200];
 mtau = _t_mtau[200];
 hinf = _t_hinf[200];
 htau = _t_htau[200];
 ninf = _t_ninf[200];
 ntau = _t_ntau[200];
 return; }
 _theta = _xi - (double)_i;
 minf = _t_minf[_i] + _theta*(_t_minf[_i+1] - _t_minf[_i]);
 mtau = _t_mtau[_i] + _theta*(_t_mtau[_i+1] - _t_mtau[_i]);
 hinf = _t_hinf[_i] + _theta*(_t_hinf[_i+1] - _t_hinf[_i]);
 htau = _t_htau[_i] + _theta*(_t_htau[_i+1] - _t_htau[_i]);
 ninf = _t_ninf[_i] + _theta*(_t_ninf[_i+1] - _t_ninf[_i]);
 ntau = _t_ntau[_i] + _theta*(_t_ntau[_i+1] - _t_ntau[_i]);
 }

__device__ double vtrap_k (_threadargsprotocommakern_ double _lx , double _ly);
__device__ void  _f_rates_k (_threadargsprotocommakern_ double _lv)
 {
   double _lalpha , _lbeta , _lsum , _lq10 ;
  _lq10 = pow( 3.0 , ( ( _dp.celsius - 6.3 ) / 10.0 ) ) ;
   _lalpha = .1 * vtrap_k ( _threadargscommakern_ - ( _lv + 40.0 ) , 10.0 ) ;
   _lbeta = 4.0 * exp ( - ( _lv + 65.0 ) / 18.0 ) ;
   _lsum = _lalpha + _lbeta ;
   mtau = 1.0 / ( _lq10 * _lsum ) ;
   minf = _lalpha / _lsum ;
   _lalpha = .07 * exp ( - ( _lv + 65.0 ) / 20.0 ) ;
   _lbeta = 1.0 / ( exp ( - ( _lv + 35.0 ) / 10.0 ) + 1.0 ) ;
   _lsum = _lalpha + _lbeta ;
   htau = 1.0 / ( _lq10 * _lsum ) ;
   hinf = _lalpha / _lsum ;
   _lalpha = .01 * vtrap_k ( _threadargscommakern_ - ( _lv + 55.0 ) , 10.0 ) ;
   _lbeta = .125 * exp ( - ( _lv + 65.0 ) / 80.0 ) ;
   _lsum = _lalpha + _lbeta ;
   ntau = 1.0 / ( _lq10 * _lsum ) ;
   ninf = _lalpha / _lsum ;
}


static int  _f_rates ( _threadargsprotocomma_ double _lv ) 
  //  double* _p; Datum* _ppvar; _cldec Datum* _thread; _NrnThread* _nt; 
  //  double _lv ;
 {
   double _lalpha , _lbeta , _lsum , _lq10 ;
  _lq10 = pow( 3.0 , ( ( celsius - 6.3 ) / 10.0 ) ) ;
   _lalpha = .1 * vtrap ( _threadargscomma_ - ( _lv + 40.0 ) , 10.0 ) ;
   _lbeta = 4.0 * exp ( - ( _lv + 65.0 ) / 18.0 ) ;
   _lsum = _lalpha + _lbeta ;
   mtau = 1.0 / ( _lq10 * _lsum ) ;
   minf = _lalpha / _lsum ;
   _lalpha = .07 * exp ( - ( _lv + 65.0 ) / 20.0 ) ;
   _lbeta = 1.0 / ( exp ( - ( _lv + 35.0 ) / 10.0 ) + 1.0 ) ;
   _lsum = _lalpha + _lbeta ;
   htau = 1.0 / ( _lq10 * _lsum ) ;
   hinf = _lalpha / _lsum ;
   _lalpha = .01 * vtrap ( _threadargscomma_ - ( _lv + 55.0 ) , 10.0 ) ;
   _lbeta = .125 * exp ( - ( _lv + 65.0 ) / 80.0 ) ;
   _lsum = _lalpha + _lbeta ;
   ntau = 1.0 / ( _lq10 * _lsum ) ;
   ninf = _lalpha / _lsum ;
    return 0; 
}
 
static int _hoc_rates() {
  double _r;
   double* _p; Datum* _ppvar; _cldec Datum* _thread; _NrnThread* _nt;
   if (_extcall_prop) {
	_p = _extcall_prop->param; 
	_ppvar = _extcall_prop->dparam;
   }else{
        _p = (double*)0;
	 _ppvar = (Datum*)0;
  }
  _thread = _extcall_thread;
  _nt = nrn_threads;
 
#if 1
 _check_rates(_threadargs_);
#endif
 _r = 1.;
 rates ( _threadargscomma_ *getarg(1) ) ;
 ret(_r);
return 0;
}
 
__device__ double vtrap_k ( _threadargsprotocommakern_ double _lx , double _ly ) 
{
   double _lvtrap;
   if ( fabs ( _lx / _ly ) < 1e-6 ) {
     _lvtrap = _ly * ( 1.0 - _lx / _ly / 2.0 ) ;
     }
   else {
     _lvtrap = _lx / ( exp ( _lx / _ly ) - 1.0 ) ;
     }
   return _lvtrap;
}
 
double vtrap ( _threadargsprotocomma_ double _lx , double _ly )
 {
   double _lvtrap;
 if ( fabs ( _lx / _ly ) < 1e-6 ) {
     _lvtrap = _ly * ( 1.0 - _lx / _ly / 2.0 ) ;
     }
   else {
     _lvtrap = _lx / ( exp ( _lx / _ly ) - 1.0 ) ;
     }
   
return _lvtrap;
 }
 
static int _hoc_vtrap() {
  double _r;
   double* _p; Datum* _ppvar; _cldec Datum* _thread; _NrnThread* _nt;
   if (_extcall_prop) {_p = _extcall_prop->param; _ppvar = _extcall_prop->dparam;}else{ _p = (double*)0; _ppvar = (Datum*)0; }
  _thread = _extcall_thread;
  _nt = nrn_threads;
 _r =  vtrap ( _threadargscomma_ *getarg(1) , *getarg(2) ) ;
 ret(_r);
 return 0;
}
 
static Pfri _ode_count(int _type) { return (Pfri)3;}
 
static Pfri _ode_spec(_NrnThread* _nt, _Memb_list* _ml, int _type) {
   double* _p; Datum* _ppvar; Datum* _thread;
   Node* _nd; int _iml, _cntml; _cldec
  _cntml = _ml->_nodecount;
  _thread = _ml->_thread;
  for (_iml = 0; _iml < _cntml; ++_iml) {
    _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
    _clb _nd = _ml->_nodelist[_iml*_cls + _clj];
    v = NODEV(_nd); _cle
/* cmc
  _clb ena = _ion_ena; _cle
  _clb ek = _ion_ek; _cle
*/
     _ode_spec1 (_threadargs_);
   }
return 0;
}
 
static Pfri _ode_map(int _ieq, double **_pv, double **_pvdot, double *_pp, Datum* _ppd, double *_atol, int _type) 
{ 
	double* _p; Datum* _ppvar; _cldec0
 	int _i; _p = _pp; _ppvar = _ppd;
	_cvode_ieq = _ieq;
	for (_i=0; _i < 3; ++_i) {
		_pv[_i] = _pp + _slist1[_i];  _pvdot[_i] = _pp + _dlist1[_i];
		_cvode_abstol(_atollist, _atol, _i);
	}
	return 0;
 }
 
static Pfri _ode_matsol(_NrnThread* _nt, _Memb_list* _ml, int _type) {
   double* _p; Datum* _ppvar; Datum* _thread;
   Node* _nd; int _iml, _cntml; _cldec
  _cntml = _ml->_nodecount;
  _thread = _ml->_thread;
  for (_iml = 0; _iml < _cntml; ++_iml) {
    _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
    _clb _nd = _ml->_nodelist[_iml*_cls + _clj];
    v = NODEV(_nd); _cle
  /* cmc _clb ena = _ion_ena; _cle
  _clb ek = _ion_ek; _cle
*/
 _ode_matsol1 (_threadargs_);
 }
return 0;
}
 
static void _thread_mem_init(Datum* _thread) {
  if (_thread1data_inuse) {
     _thread[_gth]._pval = (double*)ecalloc(6*_cls, sizeof(double));
 }else{
      _thread[_gth]._pval = _thread1data; _thread1data_inuse = 1;
 }
 }
 
static void _thread_cleanup(Datum* _thread) {
  if (_thread[_gth]._pval == _thread1data) {
   _thread1data_inuse = 0;
  }else{
   free((void*)_thread[_gth]._pval);
  }
 }

 extern void nrn_update_ion_pointer(Symbol*, Datum*, int, int, int);
 static void _update_ion_pointer(Datum* _ppvar) {

   nrn_update_ion_pointer(_na_sym, _ppvar, 0, 0, _cls);
   nrn_update_ion_pointer(_na_sym, _ppvar, 1, 3, _cls);
   nrn_update_ion_pointer(_na_sym, _ppvar, 2, 4, _cls);
   nrn_update_ion_pointer(_k_sym, _ppvar, 3, 0, _cls);
   nrn_update_ion_pointer(_k_sym, _ppvar, 4, 3, _cls);
   nrn_update_ion_pointer(_k_sym, _ppvar, 5, 4, _cls);
 }


__device__ void _hhx_initmodel_k(_threadargsprotokern_)
{
  // h = h0;
  // m = m0; 
  // n = n0; 

  rates_k ( _threadargscommakern_ v);
  m = minf ;
  h = hinf ;
  n = ninf ;
}

/*
static void initmodel(_threadargsproto_) {
  int _i; double _save;{
  _clb h = h0; _cle
  _clb m = m0; _cle
  _clb n = n0; _cle
 {
   _clb rates ( _threadargscomma_ v ) ;
   _cle _clb m = minf ;
   _cle _clb h = hinf ;
   _cle _clb n = ninf ;
   _cle }
 
}
}
*/

  
__global__ void
gpu_hhx_init_kernel(nrncuda_defines_t _dp, nrncuda_memb_prop_t mp, double t_k, double dt_k)
{
        double _rhs;
        _cldec

        int _pod  = (blockIdx.x*GPU_ADVANCE_BLOCKSIZE/GPU_PODSIZE) + (threadIdx.x >> GPU_LOGPODSIZE);
	if (_pod >= mp.num_pods) return;
        _clj  =  threadIdx.x & (GPU_PODSIZE-1);
        int podoffset = GPU_PODSIZE * _pod;
        double* _p = &_dp._params[mp.param_start_offset+podoffset*25];
        Datum* _ppvar = &_dp._dparams[mp.dparam_start_offset+podoffset*7];
        int node = _dp._nodeindices[mp.node_start_offset+podoffset + _clj];

 	v = _dp.VEC._v[node];
        ena = _ion_ena; 
        ek  = _ion_ek; 
        _hhx_initmodel_k(_threadargskern_);
        return;
}

static void nrn_init(_NrnThread* _nt, _Memb_list* _ml, int _type){
        cudaError err;
        int num_blocks;
        int num;

        /* need to work out an optimal strategy for setting up the grid based on the number of
         compartments and the number of mechanisms. But for starters, we will just use
         number of nodes. */

	nrncuda_memb_prop[_mechtype].num_pods = _ml->_nodecount;
        num_blocks = _ml->_nodecount * GPU_PODSIZE / GPU_ADVANCE_BLOCKSIZE;
        num = num_blocks * GPU_ADVANCE_BLOCKSIZE;
        if (_ml->_nodecount * GPU_PODSIZE > num) num_blocks += 1;
	nrncuda_memb_prop[_mechtype].num_blocks = num_blocks;

        dim3 dimBlock(GPU_ADVANCE_BLOCKSIZE, 1, 1);
        dim3 dimGrid(nrncuda_memb_prop[_mechtype].num_blocks, 1, 1);

	_nt->nrncuda_defines.celsius = celsius;
        gpu_hhx_init_kernel<<<dimGrid, dimBlock>>>(_nt->nrncuda_defines, nrncuda_memb_prop[_mechtype], _nt->_t, _nt->_dt);
        err = cudaGetLastError();
 
        // printf("Done with pas init\n");
}

/*
static void nrn_init(_NrnThread* _nt, _Memb_list* _ml, int _type){
double* _p; Datum* _ppvar; Datum* _thread; _cldec
Node *_nd; int* _ni; int _iml, _cntml;
   _ni = _ml->_nodeindices;
   _cntml = _ml->_nodecount;
   _thread = _ml->_thread;
   for (_iml = 0; _iml < _cntml; ++_iml) {
      _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];

#if 0
 _check_rates(_threadargs_);
#endif
     _clb v = VEC_V(_ni[_iml*_cls + _clj]); _cle
     _clb ena = _ion_ena; _cle
     _clb ek = _ion_ek; _cle
     initmodel(_threadargs_);
  }}
*/


static void _nrn_current(_threadargsprotocomma_ double* _current){ _clb _current[_clj] = 0.; _cle
{ {
   _clb gna = gnabar * m * m * m * h ;
   _cle _clb ina = gna * ( v - ena ) ;
   _cle _clb gk = gkbar * n * n * n * n ;
   _cle _clb ik = gk * ( v - ek ) ;
   _cle _clb il = gl * ( v - el ) ;
   _cle }
 _clb _current[_clj] += ina; _cle
 _clb _current[_clj] += ik; _cle
 _clb _current[_clj] += il; _cle

}}

/*
__device__ void _hhx_current(_threadargsprotocommakern_ double* _current){
   *_current = 0.;
   gna = gnabar * m * m * m * h ;
   ina = gna * ( v - ena ) ;
   gk = gkbar * n * n * n * n ;
   ik = gk * ( v - ek ) ;
   il = gl * ( v - el ) ;
   *_current += ina; 
   *_current += ik; 
   *_current += il;
}
*/

#define _hhx_current(_curr) \
   _curr = 0.; \
   _lgna = gnabar * m * m * m * h ; \
   _lina = _lgna * ( _lv - _lena ) ; \
   _lgk =  gkbar * n * n * n * n ; \
   _lik = _lgk * ( _lv - _lek ) ; \
   _lil = _lgl * ( _lv - _lel ) ; \
   _curr += _lina; \
   _curr += _lik; \
   _curr += _lil; \

__global__ void
gpu_hhx_cur_kernel(nrncuda_defines_t _dp, nrncuda_memb_prop_t mp)
{
        double _lrhs;
        _cldec

	double _lv;
	double _lgna;
	double _lgk;
	double _lgl;
	double _lena;
	double _lek;
	double _lel;

	double _lik;
	double _lina;
	double _lil;

        int _pod  = (blockIdx.x*GPU_ADVANCE_BLOCKSIZE/GPU_PODSIZE) + (threadIdx.x >> GPU_LOGPODSIZE);
	if (_pod >= mp.num_pods) return;
        _clj  =  threadIdx.x & (GPU_PODSIZE-1);
        int podoffset = GPU_PODSIZE * _pod;
        double* _p = &_dp._params[mp.param_start_offset+podoffset*25];
        Datum* _ppvar = &_dp._dparams[mp.dparam_start_offset+podoffset*7];
        int node = _dp._nodeindices[mp.node_start_offset+podoffset + _clj];

        _lv = _dp.VEC._v[node];
  
  	_lena = _ion_ena;
	_lek = _ion_ek; 
	_lel = el; 
	_lgl = gl; 
	_lv += .001; 
	_hhx_current(_g);
 	_lv -= .001; 
 	double _dik = _lik;
 	double _dina = _lina;
	_hhx_current(_lrhs);
        atomicAdd(&_ion_dinadv, (_dina - _lina)/.001);
        atomicAdd(&_ion_dikdv,  (_dik - _lik)/.001); 
	_g = (_g - _lrhs)/.001; 
        atomicAdd(&_ion_ina,  _lina); 
        atomicAdd(&_ion_ik,   _lik); 
        atomicAdd(&_dp.VEC._rhs[node], -_lrhs);
}

static void nrn_cur(_NrnThread* _nt, _Memb_list* _ml, int _type){
        cudaError err;

        dim3 dimBlock(GPU_ADVANCE_BLOCKSIZE, 1, 1);
        dim3 dimGrid(nrncuda_memb_prop[_mechtype].num_blocks, 1, 1);

        err = cudaMemcpy( _nt->nrncuda_defines.VEC._rhs,  _nt->_actual_rhs,
                          _nt->nrncuda_defines.VEC._size_rhs, cudaMemcpyHostToDevice);
        if (err != cudaSuccess) return;
        gpu_hhx_cur_kernel<<<dimGrid, dimBlock>>>(_nt->nrncuda_defines, nrncuda_memb_prop[_mechtype]);
        err = cudaGetLastError();
        if (err != cudaSuccess) return;
        err = cudaMemcpy( _nt->_actual_rhs, _nt->nrncuda_defines.VEC._rhs,
                          _nt->nrncuda_defines.VEC._size_rhs, cudaMemcpyDeviceToHost);
        if (err != cudaSuccess) return;

        // printf("Done with pas cur\n");

}


/*
static void nrn_jacob(_NrnThread* _nt, _Memb_list* _ml, int _type) {
double* _p; Datum* _ppvar; Datum* _thread; _cldec0
Node *_nd; int* _ni; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
_thread = _ml->_thread;
for (_iml = 0; _iml < _cntml; ++_iml) {
 _p = _ml->_data[_iml];
#if CACHEVEC
  if (use_cachevec) {
	_clb VEC_D(_ni[_iml*_cls + _clj]) += _g; _cle
  }else
#endif
  {
     _clb _nd = _ml->_nodelist[_iml*_cls + _clj];
	NODED(_nd) += _g; _cle
  }
 
}}
*/

__global__ void
gpu_hhx_jacob_kernel(nrncuda_defines_t _dp, nrncuda_memb_prop_t mp)
{
        double _rhs;
        _cldec

        int _pod  = (blockIdx.x*GPU_ADVANCE_BLOCKSIZE/GPU_PODSIZE) + (threadIdx.x >> GPU_LOGPODSIZE);
	if (_pod >= mp.num_pods) return;
        _clj  =  threadIdx.x & (GPU_PODSIZE-1);
        int podoffset = GPU_PODSIZE * _pod;
        double* _p = &_dp._params[mp.param_start_offset+podoffset*25];
        Datum* _ppvar = &_dp._dparams[mp.dparam_start_offset+podoffset*7];
        int node = _dp._nodeindices[mp.node_start_offset+podoffset + _clj];
        atomicAdd(&_dp.VEC._d[node], _g);
}

static void nrn_jacob(_NrnThread* _nt, _Memb_list* _ml, int _type){
        cudaError err;

        dim3 dimBlock(GPU_ADVANCE_BLOCKSIZE, 1, 1);
        dim3 dimGrid(nrncuda_memb_prop[_mechtype].num_blocks, 1, 1);

        err = cudaMemcpy( _nt->nrncuda_defines.VEC._d,  _nt->_actual_d,
                          _nt->nrncuda_defines.VEC._size_d, cudaMemcpyHostToDevice);
        if (err != cudaSuccess) return;
        gpu_hhx_jacob_kernel<<<dimGrid, dimBlock>>>(_nt->nrncuda_defines, nrncuda_memb_prop[_mechtype]);
        err = cudaGetLastError();
        if (err != cudaSuccess) return;
        err = cudaMemcpy( _nt->_actual_d, _nt->nrncuda_defines.VEC._d,
                          _nt->nrncuda_defines.VEC._size_d, cudaMemcpyDeviceToHost);
        if (err != cudaSuccess) return;

        // printf("Done with pas jacob\n");

}

/*
static void nrn_state(_NrnThread* _nt, _Memb_list* _ml, int _type) {
 double _break, _save;
double* _p; Datum* _ppvar; Datum* _thread; _cldec0
Node *_nd; int* _ni; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
_thread = _ml->_thread;
for (_iml = 0; _iml < _cntml; ++_iml) {
 _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
 _nd = _ml->_nodelist[_iml];
#if CACHEVEC
  if (use_cachevec) {
    _clb v = VEC_V(_ni[_iml*_cls + _clj]); _cle
  }else
#endif
  {
    _clb _nd = _ml->_nodelist[_iml*_cls + _clj]; v = NODEV(_nd); _cle
  }
 _break = t + .5*dt; _save = t;

{
  _clb ena = _ion_ena; _cle
  _clb ek = _ion_ek; _cle
 { {
 for (; t < _break; t += dt) {_cldec0
   states(_threadargs_);
}}
 t = _save;
 }  }}

}
*/

__global__ void
gpu_hhx_state_kernel(nrncuda_defines_t _dp, nrncuda_memb_prop_t mp, double tk, double dtk)
{
        double _rhs;
        _cldec
	double _break;
	double _save;
	double _lt;
	double _lv;

        int _pod  = (blockIdx.x*GPU_ADVANCE_BLOCKSIZE/GPU_PODSIZE) + (threadIdx.x >> GPU_LOGPODSIZE);
	if (_pod >= mp.num_pods) return;
        _clj  =  threadIdx.x & (GPU_PODSIZE-1);
        int podoffset = GPU_PODSIZE * _pod;
        double* _p = &_dp._params[mp.param_start_offset+podoffset*25];
        Datum* _ppvar = &_dp._dparams[mp.dparam_start_offset+podoffset*7];
        int node = _dp._nodeindices[mp.node_start_offset+podoffset + _clj];

        v = _dp.VEC._v[node];
	_lt = tk;
	_break = tk + .5 * dtk;  _save = tk;
 
	for (; _lt < _break; _lt += dtk) {
	    states_k(_threadargskern_, dtk); 
	}
	/* should t be in dp? */
}

static void nrn_state(_NrnThread* _nt, _Memb_list* _ml, int _type){
        cudaError err;

        dim3 dimBlock(GPU_ADVANCE_BLOCKSIZE, 1, 1);
        dim3 dimGrid(nrncuda_memb_prop[_mechtype].num_blocks, 1, 1);

        gpu_hhx_state_kernel<<<dimGrid, dimBlock>>>(_nt->nrncuda_defines, nrncuda_memb_prop[_mechtype], _nt->_t,_nt->_dt);
        err = cudaGetLastError();

        // printf("Done with pas states\n");

}


static void terminal(){}

static void _initlists(){
 double _x; double* _p = &_x; _cldec0
 int _i; static int _first = 1;
  if (!_first) return;
 _slist1[0] = &(m) - _p;  _dlist1[0] = &(Dm) - _p;
 _slist1[1] = &(h) - _p;  _dlist1[1] = &(Dh) - _p;
 _slist1[2] = &(n) - _p;  _dlist1[2] = &(Dn) - _p;
/*
   _t_minf = makevector(201*sizeof(double));
   _t_mtau = makevector(201*sizeof(double));
   _t_hinf = makevector(201*sizeof(double));
   _t_htau = makevector(201*sizeof(double));
   _t_ninf = makevector(201*sizeof(double));
   _t_ntau = makevector(201*sizeof(double));
*/
_first = 0;
}
}
